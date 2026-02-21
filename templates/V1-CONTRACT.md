# Sales Brain V1 Content Contract

This contract is the single source of truth for all Sales Brain objects.

## Global Rules

1. Every file must include YAML frontmatter.
2. Unknown or unsourced claims may be written as `To be verified` only when stating a specific fact inline (e.g., "Pipeline increased 40% | Source: To be verified"). Do not fill entire sections with "To be verified" placeholders.
3. Do not include a section if all its content would be "To be verified". Omit empty sections entirely.
4. Quantified claims must include a supporting source and a dated evidence note in the Evidence & Sources section (body) when that section is present; do not add `source_urls` in frontmatter.
5. Required sections must always exist; optional sections can be omitted when unavailable.

## Required Frontmatter (All Objects)

```yaml
---
object_type: company|target-companies|product|persona|pain-points|value-proposition|use-case|competitor|objection|case-study|sales-play
company: <company-slug>
company_display_name: <Company Name>
version: v1
last_updated: YYYY-MM-DD
last_verified: YYYY-MM-DD|To be verified
confidence: high|medium|low
tags:
  - sales-brain
---
```

- `company_display_name` is the **company** display name (e.g. "Bolt", "Gong"), not the object name (e.g. not "Sales Manager" or a product/persona name).

## Optional Frontmatter Keys (By Object)

- `product`
- `persona`
- `competitor`
- `use_case`
- `sales_stage` (discovery, evaluation, business-case, procurement, renewal)
- `buyer_journey_stage` (problem-aware, solution-aware, vendor-eval, decision)

Do not add `source_urls` to frontmatter; sources belong in the body (Evidence & Sources when present).

## Required Section Blocks (All Objects)

1. `## Overview`

## Optional Section Blocks

- `## Evidence & Sources` — Include only when there are actual sourced claims. Each evidence bullet should contain: claim, source label, date or `To be verified`.
- `## Cross-References` — Include only when there are actual links to related objects (personas, pain points, value propositions, use cases, competitors, objections, case studies, sales plays). Add links to at least 3 related objects when available.

## Evidence & Sources (when present)

- Include at least 2 evidence bullets when the section is used.
- Each evidence bullet should contain:
  - claim,
  - source label,
  - date or `To be verified`.

## Cross-References (when present)

Add links to at least 3 related objects when available:

- personas
- pain points
- value propositions
- use cases
- competitors
- objections
- case studies
- sales plays
