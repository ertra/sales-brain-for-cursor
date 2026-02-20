# Sales Brain V1 Content Contract

This contract is the single source of truth for all Sales Brain objects.

## Global Rules

1. Every file must include YAML frontmatter.
2. Unknown claims must be written as `To be verified`.
3. Quantified claims must include a supporting source in `source_urls` and a dated evidence note in the body.
4. All files should include actionable operator guidance, not only descriptive content.
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
source_urls:
  - https://example.com
tags:
  - sales-brain
---
```

## Optional Frontmatter Keys (By Object)

- `product`
- `persona`
- `competitor`
- `use_case`
- `sales_stage` (discovery, evaluation, business-case, procurement, renewal)
- `buyer_journey_stage` (problem-aware, solution-aware, vendor-eval, decision)

## Required Section Blocks (All Objects)

1. `## Overview`
2. `## Evidence & Sources`
3. `## Operator Guidance`
4. `## Cross-References`

## Evidence & Sources Block Requirements

- Include at least 2 evidence bullets.
- Each evidence bullet should contain:
  - claim,
  - source label,
  - date or `To be verified`.

## Operator Guidance Block Requirements

Include short, execution-ready bullets:

- Discovery questions (2-5)
- Disqualification criteria (2-5)
- Talk tracks (15s / 30s / 2min)
- Next-step CTA suggestions

## Cross-References Block Requirements

Add links to at least 3 related objects when available:

- personas
- pain points
- value propositions
- use cases
- competitors
- objections
- case studies
- sales plays
