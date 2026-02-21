#!/usr/bin/env python3
"""
Retrofit brain .md files: remove Operator Guidance, empty Evidence & Sources and
Cross-References, remove source_urls from frontmatter, fix company_display_name.
"""
import re
import sys
from pathlib import Path

BRAINS_DIR = Path(__file__).resolve().parent.parent / "brains"


def slug_to_display_name(slug: str) -> str:
    """Convert company slug to display name (e.g. revenue-io -> Revenue Io)."""
    return slug.replace("-", " ").title()


def is_placeholder_line(line: str) -> bool:
    """True if line is only placeholder content (To be verified, empty, or generic claim)."""
    t = line.strip()
    if not t:
        return True
    if t == "To be verified":
        return True
    if "To be verified" in t and "Source:" in t and "To be verified" in t.split("Source:")[-1].split("|")[0]:
        return True
    if re.match(r"^-\s*(Claim:)?\s*To be verified", t, re.I):
        return True
    if re.match(r"^-\s*Related\s+[\w\s]+:\s*To be verified", t, re.I):
        return True
    if re.match(r"^-\s*\d+\.\s*To be verified", t):
        return True
    if re.match(r"^-\s*\*\*\d+s\*\*:\s*To be verified", t):
        return True
    if re.match(r"^-\s*\d+s:\s*To be verified", t):
        return True
    if re.match(r"^-\s*2min:\s*To be verified", t):
        return True
    if t == "- To be verified":
        return True
    if "Claim:" in t and "To be verified" in t and "Source: To be verified" in t:
        return True
    return False


def section_content_is_placeholder(lines: list[str]) -> bool:
    """True if all non-empty lines in list are placeholder content."""
    for line in lines:
        if not line.strip():
            continue
        if line.strip().startswith("#"):
            break  # next section
        if not is_placeholder_line(line):
            return False
    return True


def remove_frontmatter_source_urls(fm: str) -> str:
    """Remove source_urls key and its value from YAML frontmatter."""
    out = []
    skip = False
    for line in fm.split("\n"):
        if line.strip().startswith("source_urls:"):
            skip = True
            continue
        if skip:
            # Skip until we hit a new top-level key (no leading space) or empty line after list
            stripped = line.strip()
            if line and not line.startswith((" ", "\t")) and stripped and not stripped.startswith("-"):
                skip = False
            elif stripped.startswith("-"):
                continue  # list item under source_urls
            else:
                continue
        out.append(line)
    return "\n".join(out)


def set_company_display_name_in_frontmatter(fm: str, company_slug: str) -> str:
    """Set company_display_name to the company display name from slug."""
    display = slug_to_display_name(company_slug)
    if "company_display_name:" in fm:
        fm = re.sub(
            r"company_display_name:\s*[\"']?[^\"'\n]+[\"']?",
            f"company_display_name: \"{display}\"",
            fm,
            count=1,
        )
    return fm


def split_frontmatter_and_body(content: str) -> tuple[str, str]:
    """Return (frontmatter, body). Frontmatter includes --- delimiters."""
    if not content.strip().startswith("---"):
        return "", content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return "", content
    return "---" + parts[1] + "---", parts[2].lstrip("\n")


def remove_section(body: str, section_name: str, until_next_heading: bool = True) -> str:
    """Remove a ## section from body. If until_next_heading, remove until next ## or EOF."""
    pattern = re.compile(
        r"\n## " + re.escape(section_name) + r"\s*\n(.*?)(?=\n## |\Z)",
        re.DOTALL,
    )
    return pattern.sub("\n", body)


def remove_operator_guidance(body: str) -> str:
    """Remove entire ## Operator Guidance section."""
    return remove_section(body, "Operator Guidance", until_next_heading=True)


def remove_evidence_sources_if_placeholder(body: str) -> str:
    """Remove ## Evidence & Sources if its content is only placeholders."""
    match = re.search(
        r"\n## Evidence & Sources\s*\n(.*?)(?=\n## |\Z)",
        body,
        re.DOTALL,
    )
    if not match:
        return body
    block = match.group(1)
    lines = block.split("\n")
    if section_content_is_placeholder(lines):
        return remove_section(body, "Evidence & Sources", until_next_heading=True)
    return body


def remove_cross_references_if_placeholder(body: str) -> str:
    """Remove ## Cross-References if its content is only placeholders."""
    match = re.search(
        r"\n## Cross-References\s*\n(.*?)(?=\n## |\Z)",
        body,
        re.DOTALL,
    )
    if not match:
        return body
    block = match.group(1)
    lines = block.split("\n")
    if section_content_is_placeholder(lines):
        return remove_section(body, "Cross-References", until_next_heading=True)
    return body


def process_file(path: Path, company_slug: str) -> bool:
    """Process one file. Return True if changed."""
    content = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter_and_body(content)
    if not fm and not content.strip().startswith("---"):
        return False  # no frontmatter, skip

    changed = False

    # Frontmatter: remove source_urls, fix company_display_name
    new_fm = remove_frontmatter_source_urls(fm)
    if new_fm != fm:
        changed = True
        fm = new_fm
    new_fm = set_company_display_name_in_frontmatter(fm, company_slug)
    if new_fm != fm:
        changed = True
        fm = new_fm

    # Body: remove Operator Guidance always
    new_body = remove_operator_guidance(body)
    if new_body != body:
        changed = True
        body = new_body

    # Body: remove Evidence & Sources and Cross-References only if placeholder-only
    new_body = remove_evidence_sources_if_placeholder(body)
    if new_body != body:
        changed = True
        body = new_body
    new_body = remove_cross_references_if_placeholder(body)
    if new_body != body:
        changed = True
        body = new_body

    if changed:
        path.write_text(fm + "\n" + body, encoding="utf-8")
    return changed


def main() -> None:
    count = 0
    for company_dir in sorted(BRAINS_DIR.iterdir()):
        if not company_dir.is_dir():
            continue
        company_slug = company_dir.name
        for md_path in company_dir.rglob("*.md"):
            if md_path.name in ("INDEX.md", "README.md"):
                continue
            try:
                if process_file(md_path, company_slug):
                    count += 1
                    print(md_path.relative_to(BRAINS_DIR))
            except Exception as e:
                print(f"Error {md_path}: {e}", file=sys.stderr)
    print(f"\nUpdated {count} files.", file=sys.stderr)


if __name__ == "__main__":
    main()
