---
description: "Sales Brain file templates for all objects. Use when creating new company files, products, personas, or any sales objects."
alwaysApply: true
---

# Sales Brain Templates

All templates are stored in the `templates/` directory. Use these as the basis for all new files:

- `templates/V1-CONTRACT.md` – global required schema and evidence rules
- `templates/company-template.md` – company.md
- `templates/product-template.md` – products/{product-name}.md
- `templates/persona-template.md` – personas/{persona-name}.md
- `templates/target-companies-template.md` – target-companies.md
- `templates/pain-points-template.md` – pain-points/{persona}-pain-points.md
- `templates/value-proposition-template.md` – value-propositions/{product}-{persona}.md
- `templates/use-case-template.md` – use-cases/{use-case}.md
- `templates/competitor-template.md` – competitors/{competitor}.md
- `templates/objection-template.md` – objections/{persona}-objections.md
- `templates/case-study-template.md` – case-studies/{customer}.md
- `templates/sales-play-template.md` – sales-plays/{play}.md

When creating or updating any sales object:

1. Read `templates/V1-CONTRACT.md` first.
2. Enforce required frontmatter and required sections.
3. Reject unsupported quantified claims; write `To be verified` when evidence is missing.
4. Include `Evidence & Sources`, `Operator Guidance`, and `Cross-References` sections.
