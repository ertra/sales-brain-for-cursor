# AiSDR Sales Brain Index

## Quick Reference
- **Company**: AiSDR Inc.
- **Website**: https://aisdr.com/
- **Positioning**: AI SDR that books qualified meetings; pipeline over activity; “AI that refuses to spam”; intent-first targeting, research-backed messaging
- **Main Sales Motions**: Founder/CEO (pipeline in days), Sales Leader (pipeline over activity), Agency/RevOps (scale without headcount)

## Available Context Files

### Always Relevant
- `company.md` — Company overview, positioning, pricing, integrations
- `target-companies.md` — ICP, industries, company sizes, named accounts, use cases

### Products (3 files)
Load when discussing specific capabilities:
- `products/aisdr-platform.md`
- `products/ai-strategist.md`
- `products/ai-prospecting.md`

### Personas (4 files)
Load when discussing buyer roles:
- `personas/sales-leader.md`
- `personas/founder-ceo.md`
- `personas/sdr.md`
- `personas/revops-agency-lead.md`

### Pain Points (4 files)
Load for discovery and problem framing:
- `pain-points/sales-leader-pain-points.md`
- `pain-points/founder-ceo-pain-points.md`
- `pain-points/sdr-pain-points.md`
- `pain-points/revops-agency-lead-pain-points.md`

### Value Propositions (4 files)
Load for messaging and ROI narrative:
- `value-propositions/aisdr-platform-sales-leader.md`
- `value-propositions/aisdr-platform-founder-ceo.md`
- `value-propositions/aisdr-platform-sdr.md`
- `value-propositions/aisdr-platform-revops-agency-lead.md`

### Use Cases (5 files)
Load for scenario-based selling:
- `use-cases/cold-outbound-multichannel.md`
- `use-cases/inbound-qualification-and-demo-booking.md`
- `use-cases/event-based-outreach.md`
- `use-cases/intent-based-outreach-and-website-visitors.md`
- `use-cases/lead-nurturing-and-reactivation.md`

### Competitors (5 files)
Load for competitive strategy:
- `competitors/11x.md`
- `competitors/artisan.md`
- `competitors/topo.md`
- `competitors/breeze.md`
- `competitors/unify.md`

### Objections (5 files)
Load for objection handling:
- `objections/common-objections.md`
- `objections/sales-leader-objections.md`
- `objections/founder-ceo-objections.md`
- `objections/sdr-objections.md`
- `objections/revops-agency-lead-objections.md`

### Case Studies (5 files)
Load when proof or references are needed:
- `case-studies/fidus-systems.md`
- `case-studies/classter.md`
- `case-studies/archangel-group.md`
- `case-studies/satchel-pulse.md`
- `case-studies/dry-runz.md`

### Sales Plays (3 files)
Load when planning or executing GTM motion:
- `sales-plays/founder-pipeline-in-days-play.md`
- `sales-plays/sales-leader-pipeline-over-activity-play.md`
- `sales-plays/agency-scale-without-headcount-play.md`

### Scraped Sources
- `scraped/` — Raw JSON (e.g. main.json from homepage)
- `scraping.log` — URLs scraped during workflow

## Loading Rules for AI Agents
- **Company/overview** → `company.md`, `target-companies.md`
- **Product question** → relevant file in `products/`
- **Persona/role** → relevant file in `personas/`, then matching `pain-points/`, `value-propositions/`, `objections/`
- **Scenario/use case** → relevant file in `use-cases/`
- **Competitive request** → relevant file in `competitors/`
- **Objection handling** → `objections/common-objections.md` then persona-specific objections
- **Proof request** → `case-studies/`
- **Execution planning** → `sales-plays/`

## Topic → File Mapping
| Topic | Primary File(s) |
|-------|------------------|
| AiSDR overview / positioning | `company.md`, `products/aisdr-platform.md` |
| Founder / pipeline in days | `personas/founder-ceo.md`, `value-propositions/aisdr-platform-founder-ceo.md`, `sales-plays/founder-pipeline-in-days-play.md`, `case-studies/dry-runz.md` |
| Sales leader / pipeline over activity | `personas/sales-leader.md`, `value-propositions/aisdr-platform-sales-leader.md`, `sales-plays/sales-leader-pipeline-over-activity-play.md`, `case-studies/fidus-systems.md`, `case-studies/classter.md` |
| SDR / one platform, get outbound right | `personas/sdr.md`, `value-propositions/aisdr-platform-sdr.md`, `pain-points/sdr-pain-points.md` |
| Agency / RevOps / scale without headcount | `personas/revops-agency-lead.md`, `value-propositions/aisdr-platform-revops-agency-lead.md`, `sales-plays/agency-scale-without-headcount-play.md`, `case-studies/archangel-group.md`, `case-studies/satchel-pulse.md` |
| Cold outbound | `use-cases/cold-outbound-multichannel.md`, `products/ai-prospecting.md` |
| Inbound / demo booking | `use-cases/inbound-qualification-and-demo-booking.md` |
| Intent / website visitors | `use-cases/intent-based-outreach-and-website-visitors.md`, `products/ai-prospecting.md` |
| Nurturing / reactivation | `use-cases/lead-nurturing-and-reactivation.md` |
| Event-based outreach | `use-cases/event-based-outreach.md` |
| AiSDR vs 11x | `competitors/11x.md`, `objections/common-objections.md` |
| Elephant in the room (cost, spam, etc.) | `objections/common-objections.md` |
| ROI / proof | `case-studies/fidus-systems.md`, `case-studies/classter.md`, `case-studies/archangel-group.md`, `case-studies/satchel-pulse.md` |

## V1 Loading Note
- Prefer files with complete `Evidence & Sources` entries.
- Treat `To be verified` claims as hypotheses, not final proof.
- G2 reviews were not scraped (HTTP 403); objections and pain points are from aisdr.com only.

---
*Last updated: 2026-02-21*
*Generated by Sales Brain*
