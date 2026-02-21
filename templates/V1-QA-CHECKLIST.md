# Sales Brain V1 QA Checklist

Use this checklist for each company folder under `brains/`.

## Required Structure Checks

- [ ] All object files include YAML frontmatter.
- [ ] `object_type` value matches file path/category.
- [ ] `version: v1` exists.
- [ ] `last_updated` and `last_verified` exist.

## Required Section Checks

- [ ] File contains `## Overview`.

## Optional Section Checks (include only when content exists)

- [ ] If `## Evidence & Sources` is present, it has real sourced claims (not all "To be verified").
- [ ] If `## Cross-References` is present, links point to existing files.

## Evidence Quality Checks

- [ ] Quantified claims have source and date when Evidence & Sources is present.
- [ ] Unsupported claims are marked `To be verified` inline, or the section is omitted.
- [ ] No section is included when all content would be "To be verified".

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
