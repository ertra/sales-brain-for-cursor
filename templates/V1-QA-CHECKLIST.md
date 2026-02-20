# Sales Brain V1 QA Checklist

Use this checklist for each company folder under `brains/`.

## Required Structure Checks

- [ ] All object files include YAML frontmatter.
- [ ] `object_type` value matches file path/category.
- [ ] `version: v1` exists.
- [ ] `last_updated` and `last_verified` exist.

## Required Section Checks

- [ ] File contains `## Evidence & Sources`.
- [ ] File contains `## Operator Guidance`.
- [ ] File contains `## Cross-References`.

## Evidence Quality Checks

- [ ] Quantified claims have source URL and date.
- [ ] Any unsupported claim is marked `To be verified`.
- [ ] Source URLs are relevant (not placeholder).

## Linking and Retrieval Checks

- [ ] Cross-reference links point to existing files.
- [ ] Persona, pain-point, value-prop, and use-case chains are present for key products.
- [ ] Competitor and objection files reference at least one case study where possible.

## Freshness Checks

- [ ] `last_verified` updated for high-impact files (`company.md`, `products/*`, `competitors/*`).
- [ ] Outdated claims are queued for re-verification.

## README/INDEX Checks

- [ ] `INDEX.md` includes V1 loading note.

## Workflow Gate Checks (/start and /continue)

- [ ] `/start` asks for company name and website URL before any scrape or file creation.
- [ ] Every phase (1-11) ends with explicit choice: continue, update, or stop.
- [ ] No phase auto-advances without explicit user confirmation.
- [ ] `/continue {company}` executes one phase, then applies the same post-phase gate.
- [ ] If user chooses update, the same phase is revised and re-reviewed before advancing.
