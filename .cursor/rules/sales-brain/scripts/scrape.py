#!/usr/bin/env python3
"""
Sales Brain - Company and Product Research Assistant
A tool for gathering and organizing sales intelligence about companies and their products.
"""
from __future__ import annotations

import os
import re
import json
import sys
import subprocess
import argparse
import time
import random
from copy import copy
from pathlib import Path
from urllib.parse import urlparse, urljoin
from datetime import datetime

SCRAPING_DEPS = ("requests", "beautifulsoup4")

# We ignore noindex and robots/bot protections for research scraping (sales intelligence only).
BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}


def _pip_install_if_missing(packages: tuple[str, ...], message: str) -> bool:
    """Try to install packages via pip. Print message to stderr, run pip with 120s timeout. Return True if pip succeeded."""
    print(message, file=sys.stderr)
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet", *packages],
            check=True,
            capture_output=True,
            timeout=120,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as e:
        print(f"Could not install dependencies: {e}", file=sys.stderr)
        return False


def _ensure_scraping_deps() -> bool:
    """Ensure scraping dependencies are installed; install via pip if missing. Return True if available."""
    try:
        import requests  # noqa: F401
        from bs4 import BeautifulSoup  # noqa: F401
        return True
    except ImportError:
        pass
    if not _pip_install_if_missing(SCRAPING_DEPS, "Installing scraping dependencies (requests, beautifulsoup4)..."):
        return False
    try:
        import requests  # noqa: F401
        from bs4 import BeautifulSoup  # noqa: F401
        return True
    except ImportError:
        print("Note: Install 'requests' and 'beautifulsoup4' for web scraping capabilities", file=sys.stderr)
        return False


def _ensure_optional_dep(pip_name: str, description: str) -> bool:
    """Ensure an optional dependency is installed; install via pip if missing. Return True if import succeeds."""
    # Try import by pip package name (e.g. curl_cffi -> import curl_cffi)
    try:
        __import__(pip_name)
        return True
    except ImportError:
        pass
    _pip_install_if_missing((pip_name,), f"Installing optional dependency ({description})...")
    try:
        __import__(pip_name)
        return True
    except ImportError:
        return False


# Lazy-init flags — dependencies are installed/imported on first use, not at import time.
_SCRAPING_AVAILABLE: bool | None = None
_CURL_CFFI_AVAILABLE: bool | None = None
_curl_requests = None  # will hold curl_cffi.requests if available


def _init_deps() -> None:
    """Lazily install and import scraping dependencies on first use."""
    global _SCRAPING_AVAILABLE, _CURL_CFFI_AVAILABLE, _curl_requests
    if _SCRAPING_AVAILABLE is not None:
        return  # already initialised

    _SCRAPING_AVAILABLE = _ensure_scraping_deps()
    if _SCRAPING_AVAILABLE:
        import requests  # noqa: F401 — imported for global availability
        from bs4 import BeautifulSoup  # noqa: F401

    _CURL_CFFI_AVAILABLE = False
    if _ensure_optional_dep("curl_cffi", "curl_cffi for Chrome impersonation"):
        try:
            from curl_cffi import requests as _cr
            _curl_requests = _cr
            _CURL_CFFI_AVAILABLE = True
        except ImportError:
            pass


def _project_root() -> Path:
    """Return the project root (directory containing templates/)."""
    script_dir = Path(__file__).resolve().parent
    # script is at .cursor/rules/sales-brain/scripts/scrape.py -> 4 levels up to project root
    return script_dir.parent.parent.parent.parent


def _load_template(name: str) -> str:
    """Load a template from the project's templates/ directory."""
    path = _project_root() / "templates" / name
    if not path.exists():
        raise FileNotFoundError(f"Template not found: {path}")
    return path.read_text(encoding="utf-8")


class SalesBrain:
    """Main class for the Sales Brain research assistant."""
    
    MAX_RETRIES = 3
    RETRY_BACKOFF = 1.0  # seconds; doubles each retry
    RETRY_JITTER = 0.5   # max random jitter added to each retry wait
    REQUEST_DELAY = 0.5  # seconds between sequential requests
    # HTTP status codes worth retrying (bot-detection often returns these spuriously)
    RETRYABLE_STATUS_CODES = {403, 404, 429, 500, 502, 503}
    
    def __init__(self, output_dir: str = "."):
        _init_deps()  # lazy install/import on first use
        self.output_dir = Path(output_dir)
        self.products_dir = self.output_dir / "products"
        self.company_file = self.output_dir / "company.md"
        self.company_data = {}
        self.products = []
        self.pages_scraped = 0
        self._session = None  # created lazily in _get_session()
        self._warned_no_cffi = False  # print curl_cffi warning only once
        
    def ensure_directories(self):
        """Create necessary directories if they don't exist."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.products_dir.mkdir(parents=True, exist_ok=True)

    def _get_session(self):
        """Return a reusable requests.Session (creates one on first call)."""
        if self._session is None:
            import requests as _req
            self._session = _req.Session()
            self._session.headers.update(BROWSER_HEADERS)
        return self._session

    def _fetch_url(self, url: str):
        """Fetch URL with retry logic and connection reuse.

        Retries on both connection-level errors (timeout, reset) and HTTP status codes
        that are commonly returned by bot-detection systems (403, 404, 429, 5xx).
        Uses Chrome TLS impersonation via curl_cffi when available; without it, Python's
        requests library has a distinctive TLS fingerprint that many WAFs reject.
        Note: 'Could not resolve host' (curl 6) means DNS failed — often due to no network.
        """
        import requests as _req

        if not _CURL_CFFI_AVAILABLE and not self._warned_no_cffi:
            self._warned_no_cffi = True
            print("   ℹ️  curl_cffi not available — using plain requests (some sites may block Python's TLS fingerprint)", file=sys.stderr)

        last_exc = None
        last_response = None
        for attempt in range(self.MAX_RETRIES):
            try:
                if _CURL_CFFI_AVAILABLE and _curl_requests is not None:
                    resp = _curl_requests.get(
                        url,
                        headers=BROWSER_HEADERS,
                        timeout=15,
                        impersonate="chrome120",
                    )
                else:
                    resp = self._get_session().get(url, timeout=15)

                # If status is OK, return immediately
                if resp.status_code not in self.RETRYABLE_STATUS_CODES:
                    return resp

                # Retryable HTTP status — retry with backoff
                last_response = resp
                if attempt < self.MAX_RETRIES - 1:
                    wait = self.RETRY_BACKOFF * (2 ** attempt) + random.uniform(0, self.RETRY_JITTER)
                    print(
                        f"   ⚠️ HTTP {resp.status_code} for {url} — retry {attempt + 1}/{self.MAX_RETRIES} (waiting {wait:.1f}s)",
                        file=sys.stderr,
                    )
                    time.sleep(wait)

            except (_req.ConnectionError, _req.Timeout) as exc:
                last_exc = exc
                last_response = None
                if attempt < self.MAX_RETRIES - 1:
                    wait = self.RETRY_BACKOFF * (2 ** attempt) + random.uniform(0, self.RETRY_JITTER)
                    print(f"   ⚠️ {type(exc).__name__} for {url} — retry {attempt + 1}/{self.MAX_RETRIES} (waiting {wait:.1f}s)", file=sys.stderr)
                    time.sleep(wait)

        # All retries exhausted — return last response if we have one, otherwise raise
        if last_response is not None:
            return last_response
        raise last_exc

    def _get_all_same_domain_links(self, soup: BeautifulSoup, base_url: str) -> list:
        """Extract all same-domain links from the page (for 1-level subpage discovery)."""
        parsed_base = urlparse(base_url)
        base_netloc = parsed_base.netloc
        seen = set()
        out = []
        for a in soup.find_all('a', href=True):
            href = a.get('href', '').strip()
            if not href or href.startswith('#') or href.startswith('javascript:'):
                continue
            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)
            # Same domain only; skip mailto, tel, etc.
            if parsed.netloc != base_netloc or parsed.scheme not in ('http', 'https'):
                continue
            # Normalize: strip fragment and trailing slash for dedupe
            path = parsed.path.rstrip('/') or '/'
            norm = f"{parsed.scheme}://{parsed.netloc}{path}"
            if norm not in seen:
                seen.add(norm)
                out.append(full_url)
        return out

    def _url_to_slug(self, url: str) -> str:
        """Convert a URL path to a safe filename slug (e.g. /solutions/sales -> solutions-sales)."""
        parsed = urlparse(url)
        path = (parsed.path or '/').strip('/')
        if not path:
            return 'home'
        slug = re.sub(r'[^a-z0-9/-]+', '-', path.lower()).strip('-')
        slug = re.sub(r'-+', '-', slug).replace('/', '-')
        return slug[:80] or 'page'

    def scrape_website(self, url: str, test_mode: bool = False, include_same_domain_links: bool = False) -> dict:
        """Scrape a website for company information. Ignores noindex and robots for research."""
        import requests as _req
        from bs4 import BeautifulSoup

        if not _SCRAPING_AVAILABLE:
            return {"error": "Scraping libraries not installed. Run: pip install requests beautifulsoup4"}
        try:
            response = self._fetch_url(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract basic information (we do not skip noindex/robots pages)
            data = {
                "url": url,
                "title": self._get_title(soup),
                "description": self._get_meta_description(soup),
                "headings": self._get_headings(soup),
                "links": self._get_important_links(soup, url),
                "text_content": self._get_main_text(soup),
                "scraped_at": datetime.now().isoformat()
            }
            if include_same_domain_links:
                data["same_domain_links"] = self._get_all_same_domain_links(soup, url)
            
            self.pages_scraped += 1
            if not test_mode:
                self._update_scraping_log(url, response.status_code)
            if test_mode:
                data["_test"] = {"request_headers": BROWSER_HEADERS, "response_status": response.status_code, "ok": True}
            return data
            
        except (_req.RequestException, OSError) as e:
            resp = getattr(e, "response", None)
            status = getattr(resp, "status_code", None) if resp is not None else None
            if not test_mode:
                self._update_scraping_log(url, status if status is not None else "error")
            err_msg = str(e)
            if "Could not resolve host" in err_msg or "curl: (6)" in err_msg:
                err_msg += " (Hint: DNS/network failed — run with network access, e.g. outside sandbox or with full_network permission.)"
            result = {"error": err_msg, "url": url}
            if test_mode:
                result["_test"] = {"request_headers": BROWSER_HEADERS, "response_status": status, "ok": False}
            return result
    
    def scrape_with_follow(self, url: str, follow: str = None, max_pages: int = 10) -> dict:
        """Scrape a URL and optionally follow discovered links.
        
        No URLs are hardcoded. We scrape the given URL (typically the homepage) once,
        extract links from that page via _get_important_links(), then follow only
        those discovered URLs that match the requested categories. Companies may use
        any paths (e.g. /about-us, /company, /our-story) — we never assume /about etc.
        
        Args:
            url: The starting URL to scrape (e.g. homepage)
            follow: Which discovered-link categories to follow: 'about', 'products', 'pricing', 'contact', 'all', or None
            max_pages: Maximum number of pages to scrape (default 10)
        
        Returns:
            Dict with 'main' page data and 'followed' list of additional pages
        """
        parsed_base = urlparse(url)
        base_domain = parsed_base.netloc

        # First scrape: get the page (usually homepage); all followed URLs come from links on this page
        print(f"🔍 Scraping: {url}", file=sys.stderr)
        main_data = self.scrape_website(url)

        result = {
            "main": main_data,
            "followed": [],
            "total_pages": 1
        }

        if "error" in main_data or not follow:
            return result

        # Category names only — actual URLs come from main_data["links"] (discovered from page)
        if follow == "all":
            categories = ["about", "products", "pricing", "contact"]
        else:
            categories = [cat.strip() for cat in follow.split(",")]

        urls_to_follow = []
        scraped_urls = {url}

        for category in categories:
            if category in main_data.get("links", {}):
                for link in main_data["links"][category]:
                    link_url = link.get("url", "")
                    parsed_link = urlparse(link_url)
                    if parsed_link.netloc == base_domain and link_url not in scraped_urls:
                        urls_to_follow.append({
                            "url": link_url,
                            "category": category,
                            "text": link.get("text", "")
                        })
                        scraped_urls.add(link_url)
        
        # Scrape followed URLs (up to max_pages - 1, since we already scraped main)
        for link_info in urls_to_follow[:max_pages - 1]:
            link_url = link_info["url"]
            print(f"🔍 Following [{link_info['category']}]: {link_url}", file=sys.stderr)
            time.sleep(self.REQUEST_DELAY)
            
            followed_data = self.scrape_website(link_url)
            followed_data["_category"] = link_info["category"]
            followed_data["_link_text"] = link_info["text"]
            result["followed"].append(followed_data)
            result["total_pages"] += 1
        
        return result

    def scrape_homepage_with_subpages(self, url: str, max_subpages: int = 30, test_mode: bool = False) -> dict:
        """Scrape the given URL (homepage) and all 1-level same-domain subpages. Saves each page to output_dir/scraped/ for later use."""
        if not _SCRAPING_AVAILABLE:
            return {"error": "Scraping libraries not installed. Run: pip install requests beautifulsoup4"}
        # Normalize main URL (strip fragment)
        parsed_main = urlparse(url)
        main_url = f"{parsed_main.scheme}://{parsed_main.netloc}{parsed_main.path.rstrip('/') or ''}"
        base_netloc = parsed_main.netloc

        print(f"🔍 Scraping homepage: {main_url}", file=sys.stderr)
        main_data = self.scrape_website(main_url, test_mode=test_mode, include_same_domain_links=True)
        if "error" in main_data:
            return {"main": main_data, "subpages": [], "index": {}, "total_pages": 1}

        subpage_urls = main_data.get("same_domain_links", [])
        # Dedupe and exclude main URL and common non-content paths
        skip_paths = ('/', '', '/#', '/#/', '/login', '/signin', '/logout', '/register', '/cart')
        seen = {main_url}
        to_scrape = []
        for u in subpage_urls:
            p = urlparse(u)
            path = (p.path or '/').rstrip('/') or '/'
            if p.netloc != base_netloc or u in seen:
                continue
            if path in skip_paths or path.startswith('/#'):
                continue
            seen.add(u)
            to_scrape.append(u)
        to_scrape = to_scrape[:max_subpages]

        scraped_dir = self.output_dir / "scraped"
        if not test_mode:
            scraped_dir.mkdir(parents=True, exist_ok=True)
            # Save main (without same_domain_links for smaller file; keep it in memory for index)
            main_to_save = {k: v for k, v in main_data.items() if k != "same_domain_links"}
            (scraped_dir / "main.json").write_text(json.dumps(main_to_save, indent=2), encoding='utf-8')
            print(f"   ✅ Saved: {scraped_dir / 'main.json'}", file=sys.stderr)

        index = {"main_url": main_url, "scraped_at": datetime.now().isoformat(), "subpages": []}
        subpages_data = []

        for i, sub_url in enumerate(to_scrape):
            slug = self._url_to_slug(sub_url)
            print(f"   [{i+1}/{len(to_scrape)}] {sub_url}", file=sys.stderr)
            time.sleep(self.REQUEST_DELAY)
            data = self.scrape_website(sub_url, test_mode=test_mode)
            subpages_data.append({"url": sub_url, "slug": slug, "data": data})
            if not test_mode:
                out_path = scraped_dir / f"{slug}.json"
                to_save = data
                out_path.write_text(json.dumps(to_save, indent=2), encoding='utf-8')
                index["subpages"].append({"url": sub_url, "slug": slug, "file": f"{slug}.json"})

        if not test_mode:
            (scraped_dir / "index.json").write_text(json.dumps(index, indent=2), encoding='utf-8')
            print(f"   ✅ Index: {scraped_dir / 'index.json'} ({len(index['subpages'])} subpages)", file=sys.stderr)

        return {
            "main": main_data,
            "subpages": subpages_data,
            "index": index,
            "total_pages": 1 + len(subpages_data),
        }

    def load_scraped_dir(self) -> dict | None:
        """Load existing scraped data from output_dir/scraped/ if present. Returns same shape as scrape_homepage_with_subpages, or None if not found."""
        scraped_dir = self.output_dir / "scraped"
        index_path = scraped_dir / "index.json"
        main_path = scraped_dir / "main.json"
        if not index_path.exists() or not main_path.exists():
            return None
        try:
            index = json.loads(index_path.read_text(encoding="utf-8"))
            main_data = json.loads(main_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return None
        subpages_data = []
        for entry in index.get("subpages", []):
            slug = entry.get("slug")
            path = scraped_dir / entry.get("file", f"{slug}.json")
            if not path.exists():
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                subpages_data.append({"url": entry.get("url", ""), "slug": slug, "data": data})
            except (json.JSONDecodeError, OSError):
                continue
        return {
            "main": main_data,
            "subpages": subpages_data,
            "index": index,
            "total_pages": 1 + len(subpages_data),
        }

    def merge_links_from_pages(self, pages: list[dict]) -> dict:
        """Merge 'links' from multiple page dicts (main + subpages) for product detection etc."""
        merged = {}
        for page in pages:
            links = page.get("links") or {}
            for category, items in links.items():
                if not isinstance(items, list):
                    continue
                merged.setdefault(category, [])
                seen_urls = {x["url"] for x in merged[category] if isinstance(x, dict) and "url" in x}
                for item in items:
                    if isinstance(item, dict) and item.get("url") not in seen_urls:
                        merged[category].append(item)
                        seen_urls.add(item.get("url"))
        return merged

    def get_scraped_pages_for_phase(self, phase: str) -> list[dict] | None:
        """Return list of page data from scraped/ relevant to a phase (products, personas, case-studies, etc.), or None if no scraped dir."""
        data = self.load_scraped_dir()
        if not data:
            return None
        # Slug/URL keywords that suggest relevance per phase (phase name -> keywords in path/slug)
        phase_keywords = {
            "company": ("main", "about", "company"),
            "products": ("product", "platform", "pricing", "solution", "collective"),
            "target-companies": ("customer", "industry", "industries", "case-studies"),
            "personas": ("solution", "for-sales", "for-marketing", "revenue", "role"),
            "pain-points": ("challenge", "why", "reviews"),
            "value-propositions": ("roi", "testimonial", "value"),
            "use-cases": ("use-case", "case-studies", "solution"),
            "competitors": (),  # usually external URLs
            "objections": ("reviews", "faq"),
            "case-studies": ("case-studies", "customer", "story"),
            "sales-plays": (),  # synthesis
        }
        keywords = phase_keywords.get(phase.lower(), ())
        if not keywords:
            return [data["main"]] + [s["data"] for s in data["subpages"]]
        out = []
        main_slug = "main"
        if any(k in main_slug for k in keywords) or phase.lower() == "company":
            out.append(data["main"])
        for s in data["subpages"]:
            slug = (s.get("slug") or "").lower()
            url = (s.get("url") or "").lower()
            if any(k in slug or k in url for k in keywords):
                out.append(s["data"])
        return out if out else None

    def _update_scraping_log(self, url: str, status):
        """Log the scraped URL and HTTP status to scraping.log."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = self.output_dir / "scraping.log"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status_str = str(status)
        ok = "ok" if (isinstance(status, int) and 200 <= status < 300) else "not ok"
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {url} {status_str} {ok}\n")
    
    def _get_title(self, soup: BeautifulSoup) -> str:
        """Extract page title."""
        title = soup.find('title')
        return title.get_text().strip() if title else ""
    
    def _get_meta_description(self, soup: BeautifulSoup) -> str:
        """Extract meta description."""
        meta = soup.find('meta', attrs={'name': 'description'})
        if meta:
            return meta.get('content', '')
        
        # Try Open Graph description
        og_desc = soup.find('meta', attrs={'property': 'og:description'})
        if og_desc:
            return og_desc.get('content', '')
        
        return ""
    
    def _get_headings(self, soup: BeautifulSoup) -> list:
        """Extract all headings in document order."""
        headings = []
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            text = heading.get_text().strip()
            if text:
                headings.append({"level": heading.name, "text": text})
        return headings[:20]  # Limit to first 20
    
    def _get_important_links(self, soup: BeautifulSoup, base_url: str) -> dict:
        """Extract important navigation links from the page. No hardcoded URLs — we only
        collect <a href="..."> present in the page and classify them by keyword match
        on link text/href (e.g. 'about' matches /about-us, /company, /our-story)."""
        links = {
            "about": [],
            "products": [],
            "pricing": [],
            "contact": [],
            "other": []
        }
        seen_urls: dict[str, set[str]] = {cat: set() for cat in links}

        keywords = {
            "about": ["about", "company", "team", "story", "mission"],
            "products": ["product", "solution", "service", "feature", "platform"],
            "pricing": ["pricing", "price", "plan", "cost"],
            "contact": ["contact", "support", "help"]
        }

        for a in soup.find_all('a', href=True):
            href = a.get('href', '')
            text = a.get_text().strip().lower()
            
            if not href or href.startswith('#') or href.startswith('javascript:'):
                continue
                
            full_url = urljoin(base_url, href)
            
            categorized = False
            for category, kws in keywords.items():
                if any(kw in text or kw in href.lower() for kw in kws):
                    if full_url not in seen_urls[category]:
                        seen_urls[category].add(full_url)
                        links[category].append({
                            "text": a.get_text().strip(),
                            "url": full_url
                        })
                    categorized = True
                    break

            if not categorized and full_url not in seen_urls["other"]:
                seen_urls["other"].add(full_url)
                links["other"].append({
                    "text": a.get_text().strip(),
                    "url": full_url
                })
        
        # Limit results
        for category in links:
            links[category] = links[category][:5]
            
        return links
    
    def _get_main_text(self, soup: BeautifulSoup) -> str:
        """Extract main text content (operates on a copy to avoid mutating the original soup)."""
        soup_copy = copy(soup)
        for element in soup_copy(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        text = soup_copy.get_text(separator=' ', strip=True)
        # Clean up whitespace
        text = re.sub(r'\s+', ' ', text)
        return text[:5000]  # Limit to first 5000 chars
    
    def generate_company_md(self, company_name: str, url: str, scraped_data: dict = None) -> str:
        """Generate company.md content from templates/company-template.md."""
        template = _load_template("company-template.md")
        subs = {
            "{Company Name}": company_name,
            "{2-3 sentence company description}": scraped_data.get("description", "[To be filled based on research]") if scraped_data else "[To be filled based on research]",
            "{Primary industry}": "[To be determined]",
            "{Year}": "[Unknown]",
            "{Location}": "[Unknown]",
            "{Employee range}": "[Unknown]",
            "{Statement}": "[To be determined from research]",
            "{Customer segments}": "[To be determined]",
            "{Unique selling points}": "[To be determined]",
            "{URL}": url,
            "{Page title}": scraped_data.get("title", "N/A") if scraped_data else "N/A",
            "{Headings from scraped page}": self._format_headings(scraped_data.get("headings", [])) if scraped_data else "N/A",
            "{Links from scraped page}": self._format_links(scraped_data.get("links", {})) if scraped_data else "N/A",
            "{Other relevant info}": f"- Research date: {datetime.now().strftime('%Y-%m-%d')}\n- Status: Pending review",
            "{date}": datetime.now().strftime("%Y-%m-%d"),
        }
        for placeholder, value in subs.items():
            template = template.replace(placeholder, value)
        return template
    
    def _format_headings(self, headings: list) -> str:
        """Format headings for markdown."""
        if not headings:
            return "None found"
        return "\n".join([f"- [{h['level'].upper()}] {h['text']}" for h in headings])
    
    def _format_links(self, links: dict) -> str:
        """Format links for markdown."""
        output = []
        for category, items in links.items():
            if items:
                output.append(f"\n**{category.title()}:**")
                for link in items:
                    output.append(f"- [{link['text']}]({link['url']})")
        return "\n".join(output) if output else "None found"
    
    def generate_product_md(self, product_name: str, company_name: str,
                           features: list = None, problem: str = None,
                           value_prop: str = None, competition: list = None) -> str:
        """Generate product markdown content from templates/product-template.md."""
        features_md = "\n".join([f"- {f}" for f in (features or ["[To be determined]"])])
        if competition:
            competition_rows = "\n".join(
                f"| {comp.get('name', 'Unknown')} | {comp.get('difference', 'TBD')} |"
                for comp in competition
            )
        else:
            competition_rows = "| [To be researched] | [To be determined] |"
        template = _load_template("product-template.md")
        subs = {
            "{Product Name}": product_name,
            "{Company name – when used under a company folder}": company_name,
            "{Product description}": "[Product description to be researched]",
            "{Main Features}": features_md,
            "{Customer problem addressed}": problem or "[What customer problem does this solve?]",
            "{Unique value delivered}": value_prop or "[What unique value does this product provide?]",
            "{Ideal customer profile}": "[Ideal customer profile to be determined]",
            "{Competition table}": competition_rows,
            "{If available}": "[To be researched if publicly available]",
            "{Other info}": f"- Research date: {datetime.now().strftime('%Y-%m-%d')}\n- Status: Pending review",
            "{date}": datetime.now().strftime("%Y-%m-%d"),
        }
        for placeholder, value in subs.items():
            template = template.replace(placeholder, value)
        return template
    
    def save_company(self, content: str):
        """Save company.md file."""
        self.ensure_directories()
        self.company_file.write_text(content, encoding='utf-8')
        print(f"✅ Saved: {self.company_file}")
    
    def save_product(self, product_name: str, content: str):
        """Save product markdown file."""
        self.ensure_directories()
        # Create slug from product name
        slug = re.sub(r'[^a-z0-9]+', '-', product_name.lower()).strip('-')
        product_file = self.products_dir / f"{slug}.md"
        product_file.write_text(content, encoding='utf-8')
        print(f"✅ Saved: {product_file}")
        return product_file
    
    def load_company(self) -> str | None:
        """Load existing company.md if it exists."""
        if self.company_file.exists():
            return self.company_file.read_text(encoding='utf-8')
        return None
    
    def list_products(self) -> list:
        """List all product files."""
        if not self.products_dir.exists():
            return []
        return list(self.products_dir.glob("*.md"))
    
    def interactive_start(self):
        """Start interactive mode."""
        print("\n" + "="*50)
        print("🧠 SALES BRAIN - Company Research Assistant")
        print("="*50 + "\n")
        
        # Get company info
        company_name = input("Enter company name: ").strip()
        if not company_name:
            print("❌ Company name is required")
            return
            
        website_url = input("Enter website URL: ").strip()
        if not website_url:
            print("❌ Website URL is required")
            return
            
        # Ensure URL has protocol
        if not website_url.startswith(('http://', 'https://')):
            website_url = 'https://' + website_url
        
        print(f"\n🔍 Researching {company_name}...")
        
        # Use existing scraped/ data if available; otherwise scrape now
        scraped_data = None
        loaded = self.load_scraped_dir()
        if loaded:
            print("   📂 Using existing scraped data from scraped/ (main + {} subpages)".format(len(loaded["subpages"])), file=sys.stderr)
            scraped_data = dict(loaded["main"])
            # Merge links from all pages for product detection
            all_pages = [loaded["main"]] + [s["data"] for s in loaded["subpages"]]
            scraped_data["links"] = self.merge_links_from_pages(all_pages)
        if scraped_data is None:
            scraped_data = self.scrape_website(website_url)
            if "error" in scraped_data:
                print(f"⚠️ Scraping warning: {scraped_data['error']}")
                scraped_data = None
        
        # Generate and save company.md
        company_content = self.generate_company_md(company_name, website_url, scraped_data)
        self.save_company(company_content)
        
        # Show to user
        print("\n" + "-"*50)
        print("📄 COMPANY INFORMATION")
        print("-"*50)
        print(company_content[:2000] + "..." if len(company_content) > 2000 else company_content)
        
        # Confirmation loop
        while True:
            response = input("\n✅ Does this look accurate? (yes/no): ").strip().lower()
            
            if response in ['yes', 'y']:
                print("\n✅ Company information confirmed!")
                break
            elif response in ['no', 'n']:
                changes = input("What should be changed? (describe the changes): ").strip()
                print(f"\n📝 Note: Please manually edit company.md with these changes: {changes}")
                print(f"   File location: {self.company_file.absolute()}")
                input("Press Enter after making changes...")
                
                # Reload and show again
                updated_content = self.load_company()
                if updated_content:
                    print("\n" + "-"*50)
                    print("📄 UPDATED COMPANY INFORMATION")
                    print("-"*50)
                    print(updated_content[:2000] + "..." if len(updated_content) > 2000 else updated_content)
            else:
                print("Please enter 'yes' or 'no'")
        
        # Product detection
        print("\n🔍 Detecting products...")
        self._detect_products(company_name, scraped_data)
    
    def _detect_products(self, company_name: str, scraped_data: dict = None):
        """Detect and create product files."""
        # Check if we have product links
        product_links = []
        if scraped_data and 'links' in scraped_data:
            product_links = scraped_data['links'].get('products', [])
        
        if product_links:
            print(f"\n📦 Found {len(product_links)} potential product pages:")
            for i, link in enumerate(product_links, 1):
                print(f"   {i}. {link['text']} - {link['url']}")
        
        # Ask user to identify products
        print("\n📝 Let's identify the products.")
        print("Enter product names one at a time (or 'done' to finish):\n")
        
        products = []
        while True:
            product_name = input("Product name (or 'done'): ").strip()
            
            if product_name.lower() == 'done':
                break
            
            if product_name:
                products.append(product_name)
                print(f"   ✅ Added: {product_name}")
        
        if not products:
            print("\n⚠️ No products added. You can add them later with /add product")
            return
        
        # Create product files
        print(f"\n📁 Creating {len(products)} product files...")
        
        for product_name in products:
            content = self.generate_product_md(product_name, company_name)
            product_file = self.save_product(product_name, content)
        
        print(f"\n✅ Created {len(products)} product files in {self.products_dir}")
        print("\n📋 Product Summary:")
        for pf in self.list_products():
            print(f"   - {pf.name}")
        
        print("\n🎉 Sales Brain setup complete!")
        print(f"   Company file: {self.company_file}")
        print(f"   Products dir: {self.products_dir}")
        print(f"\n📊 Total pages scraped: {self.pages_scraped}")


def _print_test_summary(data: dict, url: str):
    """Print verbose test summary to stderr."""
    t = data.get("_test", {})
    status = t.get("response_status")
    ok = t.get("ok", False)
    status_str = str(status) if status is not None else "error"
    print("\n" + "=" * 60, file=sys.stderr)
    print("TEST MODE – no log file written", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print(f"URL:        {url}", file=sys.stderr)
    print(f"Status:     {status_str}  {'ok' if ok else 'not ok'}", file=sys.stderr)
    if "error" in data:
        print(f"Error:      {data['error']}", file=sys.stderr)
    elif data.get("title"):
        print(f"Title:      {data['title'][:70]}{'…' if len(data.get('title', '')) > 70 else ''}", file=sys.stderr)
    print("Request headers:", file=sys.stderr)
    for k, v in (t.get("request_headers") or {}).items():
        print(f"  {k}: {v[:60]}{'…' if len(v) > 60 else ''}", file=sys.stderr)
    print("=" * 60 + "\n", file=sys.stderr)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Sales Brain - Company and Product Research Assistant"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Start command
    start_parser = subparsers.add_parser('start', help='Start interactive research')
    start_parser.add_argument('--output', '-o', default='.', help='Output directory (e.g. brains/company-slug/; default: current directory)')
    
    # Scrape command
    scrape_parser = subparsers.add_parser('scrape', help='Scrape a URL')
    scrape_parser.add_argument('url', help='URL to scrape')
    scrape_parser.add_argument('--output', '-o', help='Output JSON file')
    scrape_parser.add_argument('--log-dir', '-d', default='.', help='Directory for scraping.log (e.g. brains/company-slug/; default: current directory)')
    scrape_parser.add_argument('--follow', '-f', 
                               help='Follow discovered links: about, products, pricing, contact, all (comma-separated)')
    scrape_parser.add_argument('--max-pages', '-m', type=int, default=10,
                               help='Maximum pages to scrape when following links (default: 10)')
    scrape_parser.add_argument('--test', '-t', action='store_true',
                               help='Test mode: verbose output, no log file write')
    scrape_parser.add_argument('--subpages', '-s', action='store_true',
                               help='Scrape homepage plus 1 level of same-domain subpages; save each to -d/scraped/ for later use')
    scrape_parser.add_argument('--max-subpages', type=int, default=30,
                               help='Max subpages to scrape when using --subpages (default: 30)')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List products')
    list_parser.add_argument('--dir', '-d', default='.', help='Directory to search (e.g. brains/company-slug/; default: current directory)')

    # Load-scraped command: summarize existing scraped/ dir for use by workflow steps
    load_parser = subparsers.add_parser('load-scraped', help='Summarize existing scraped/ data (for workflow: check before scraping)')
    load_parser.add_argument('--dir', '-d', default='.', help='Company directory (e.g. brains/company-slug/; default: current directory)')
    load_parser.add_argument('--phase', '-p', help='Filter pages relevant to phase: company, products, personas, case-studies, etc.')
    
    args = parser.parse_args()
    
    if args.command == 'start':
        brain = SalesBrain(args.output)
        brain.interactive_start()
        
    elif args.command == 'scrape':
        brain = SalesBrain(args.log_dir)
        test_mode = getattr(args, 'test', False)
        use_subpages = getattr(args, 'subpages', False)
        max_subpages = getattr(args, 'max_subpages', 30)
        
        if use_subpages and not test_mode:
            # Homepage + 1 level of subpages; saves to -d/scraped/
            data = brain.scrape_homepage_with_subpages(args.url, max_subpages=max_subpages, test_mode=False)
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    json.dump({"main": data["main"], "index": data["index"], "total_pages": data["total_pages"]}, f, indent=2)
                print(f"✅ Summary saved to {args.output}", file=sys.stderr)
            else:
                # Print summary only (full page content is in scraped/*.json)
                print(json.dumps({"main_url": data["index"]["main_url"], "total_pages": data["total_pages"], "subpages": data["index"]["subpages"], "scraped_dir": str(Path(args.log_dir) / "scraped")}, indent=2))
        elif args.follow and not test_mode:
            # Use follow mode to scrape multiple pages (no test mode for follow)
            data = brain.scrape_with_follow(args.url, follow=args.follow, max_pages=args.max_pages)
        else:
            # Single page scrape
            data = brain.scrape_website(args.url, test_mode=test_mode)
        
        if test_mode and "_test" in data:
            _print_test_summary(data, args.url)
        
        if not use_subpages:
            if args.output and not test_mode:
                with open(args.output, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
                print(f"✅ Saved to {args.output}", file=sys.stderr)
            elif not test_mode:
                print(json.dumps(data, indent=2))
            elif test_mode:
                out = {k: v for k, v in data.items() if k != "_test"}
                print(json.dumps(out, indent=2))
        
        print(f"\n📊 Total pages scraped: {brain.pages_scraped}", file=sys.stderr)
            
    elif args.command == 'list':
        brain = SalesBrain(args.dir)
        products = brain.list_products()
        
        if products:
            print(f"📦 Found {len(products)} products:")
            for p in products:
                print(f"   - {p.name}")
        else:
            print("No products found")

    elif args.command == 'load-scraped':
        brain = SalesBrain(args.dir)
        phase = getattr(args, 'phase', None)
        if phase:
            pages = brain.get_scraped_pages_for_phase(phase)
            if pages is None:
                print(json.dumps({"ok": False, "reason": "no_scraped_dir", "phase": phase}))
            else:
                summary = [{"title": p.get("title", ""), "url": p.get("url", "")} for p in pages if isinstance(p, dict)]
                print(json.dumps({"ok": True, "phase": phase, "count": len(pages), "pages": summary}, indent=2))
        else:
            data = brain.load_scraped_dir()
            if data is None:
                print(json.dumps({"ok": False, "reason": "no_scraped_dir"}))
            else:
                index = data["index"]
                subpages = [{"slug": s.get("slug"), "url": s.get("url")} for s in index.get("subpages", [])]
                print(json.dumps({
                    "ok": True,
                    "main_url": index.get("main_url"),
                    "scraped_at": index.get("scraped_at"),
                    "total_pages": data["total_pages"],
                    "subpages": subpages,
                }, indent=2))
            
    else:
        # Default: start interactive mode
        brain = SalesBrain()
        brain.interactive_start()


if __name__ == "__main__":
    main()
