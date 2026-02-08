# Apollo Sales Brain Index

## Quick Reference
- **Company**: Apollo (Apollo.io)
- **Website**: https://www.apollo.io/
- **Positioning**: The AI sales platform for smarter, faster revenue growth—data, outbound, inbound, and deal execution in one platform
- **Main Products**: Apollo Data, Outbound, Inbound, Data Enrichment, Deal Execution

## Available Context Files

### Always Relevant
- `company.md` — Company overview, mission, target market, differentiators, compliance
- `target-companies.md` — Target segments (startups/SMB, mid-market, enterprise, sales-led, RevOps)

### Products (5 files)
Load when user asks about a specific product or capability:
- `products/apollo-data.md` — B2B data network; 210M+ contacts, 91% email accuracy, 65+ data points
- `products/outbound.md` — Outbound sales software; AI campaigns, sequences, dialer, deliverability
- `products/inbound.md` — Inbound lead conversion; visitor ID, form enrichment, routing, scheduler
- `products/data-enrichment.md` — B2B data enrichment; waterfall, AI Research, CRM/API sync
- `products/deal-execution.md` — Sales execution; pre-meeting insights, call recording, pipeline, coaching

### Personas (4 files)
Load when discussing a specific role or buyer:
- `personas/sales-leader.md` — VP Sales, BDR Leader; pipeline, stack consolidation, rep productivity
- `personas/marketer.md` — Demand gen, growth; inbound, routing, enrichment
- `personas/sdr-bdr.md` — SDR/BDR; daily workflow, lists, sequences, dialer
- `personas/revenue-operations.md` — RevOps; data quality, enrichment, stack consolidation

### Pain Points (4 files)
Load when uncovering or addressing pains:
- `pain-points/sales-leader-pain-points.md` — Manual prospecting, stack sprawl, no pipeline/coaching visibility
- `pain-points/sdr-bdr-pain-points.md` — Manual research, too many tools, deliverability, priorities
- `pain-points/marketer-pain-points.md` — Hot leads go cold, anonymous visitors, disconnected tools
- `pain-points/revenue-operations-pain-points.md` — Stale data, multiple vendors, CRM out of sync

### Value Propositions (5 files)
Load when crafting messaging or "why Apollo":
- `value-propositions/outbound-sales-leader.md` — Book more meetings, 50% cost savings, 4x SDR efficiency
- `value-propositions/outbound-sdr-bdr.md` — One platform, 75% more meetings, 50% less manual work
- `value-propositions/inbound-marketer.md` — Don't let hot leads go cold; 300% routing; one platform
- `value-propositions/data-enrichment-revenue-operations.md` — 50% data quality, half the cost; Census, Built In
- `value-propositions/deal-execution-sales-leader.md` — 50% less manual work; pipeline visibility; Cyera, FLO EV

### Use Cases (5 files)
Load when discussing a scenario or "when would we use Apollo":
- `use-cases/scale-outbound-without-headcount.md` — 4x SDR efficiency, 75% more meetings; GTM Ops, Cyera
- `use-cases/consolidate-sales-tech-stack.md` — Replace ZoomInfo + Outreach; 50%+ savings; Predictable Revenue, Census
- `use-cases/improve-data-quality-enrichment-at-scale.md` — 50% data quality, 100k enriched daily; Census, Built In, Leadium
- `use-cases/convert-inbound-leads-faster.md` — 300% routing; visitor ID, form enrichment; don't let hot leads go cold
- `use-cases/close-deals-with-less-manual-work.md` — 50% less manual work; call insights, pipeline; Cyera, FLO EV, Bitrise

### Competitors (3 files)
Load when competing or displacing:
- `competitors/zoominfo.md` — #1 GTM platform; Apollo wins on enrichment quality, one platform, 50%+ savings
- `competitors/outreach.md` — AI Revenue Workflow; Apollo wins on data included, one contract
- `competitors/salesloft.md` — Revenue orchestration; Apollo wins on data included, one platform

### Objections (5 files)
Load when handling objections:
- `objections/common-objections.md` — Data/quality, price, timing, competition, status quo, authority
- `objections/sales-leader-objections.md` — Headcount, price, timing, ZoomInfo+Outreach, status quo, authority
- `objections/revenue-operations-objections.md` — Data standard, procurement, timing, benchmark, integrations, security
- `objections/sdr-bdr-objections.md` — Workflow, price, timing, Outreach/Salesloft, manager, decision-maker
- `objections/marketer-objections.md` — Routing tool, budget, timing, HubSpot/Marketo, conversion, alignment

### Case Studies (3 files)
Load when proof or reference is needed:
- `case-studies/predictable-revenue.md` — 50% cost savings; 2x open rate; 50% faster time to meeting; ZoomInfo+Outreach → Apollo
- `case-studies/census.md` — 50% data quality, 64% cost savings; benchmark vs ZoomInfo, Clearbit, Lusha, Seamless
- `case-studies/cyera.md` — 75% more meetings, 50% less manual work, 4+ hrs saved/day; 100+ reps

### Sales Plays (3 files)
Load when executing a play or planning outreach:
- `sales-plays/consolidation-play.md` — Replace ZoomInfo + Outreach; Sales Leader, RevOps; renewal trigger
- `sales-plays/scale-outbound-play.md` — Scale outbound without headcount; Sales Leader; 75% more meetings, 4x SDR
- `sales-plays/data-quality-revops-play.md` — Data quality & RevOps; Census/Built In story; enrichment renewal

## Loading Rules for AI Agents
- **Company or overview** → `company.md`, `target-companies.md`
- **Product question** → relevant file in `products/`
- **Persona or role** → relevant file in `personas/`, then `pain-points/`, `value-propositions/`, `objections/` for that persona
- **Use case or scenario** → relevant file in `use-cases/`
- **Competitor** → relevant file in `competitors/`
- **Objection** → `objections/common-objections.md` then persona-specific in `objections/`
- **Proof or reference** → `case-studies/`
- **Play or sequence** → `sales-plays/`

## Topic → File Mapping
| Topic | Primary File(s) |
|-------|------------------|
| Apollo Data, B2B data, enrichment | products/apollo-data.md, products/data-enrichment.md |
| Outbound, sequences, dialer, meetings | products/outbound.md, value-propositions/outbound-sales-leader.md |
| Inbound, routing, form enrichment | products/inbound.md, value-propositions/inbound-marketer.md |
| Deal execution, call insights, pipeline | products/deal-execution.md, value-propositions/deal-execution-sales-leader.md |
| Consolidation, replace ZoomInfo + Outreach | use-cases/consolidate-sales-tech-stack.md, case-studies/census.md, case-studies/predictable-revenue.md |
| Scale outbound, 4x SDR, 75% more meetings | use-cases/scale-outbound-without-headcount.md, case-studies/cyera.md |
| Data quality, RevOps, Census | value-propositions/data-enrichment-revenue-operations.md, case-studies/census.md |
| ZoomInfo / Outreach / Salesloft | competitors/zoominfo.md, competitors/outreach.md, competitors/salesloft.md |
| Price, timing, competition objections | objections/common-objections.md |
| Predictable Revenue, Census, Cyera | case-studies/ |

---
*Last updated: 2026-02-08*
*Generated by Sales Brain*
