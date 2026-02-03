# Gong Sales Brain Index

## Quick Reference
- **Company**: Gong
- **Website**: https://www.gong.io/
- **Positioning**: Revenue AI OS — #1 AI operating system for revenue teams; Leader in 2025 Gartner Magic Quadrant for Revenue Action Orchestration
- **Main Products**: Revenue Graph, Engage, Forecast, Agents, Collective

## Available Context Files

### Always Relevant
- `company.md` — Company overview, positioning, target market, differentiators
- `target-companies.md` — Target customer profiles (Technology, Financial Services, Healthcare, Enterprise GTM)

### Products (5 files)
Load when user asks about a specific product or capability:
- `products/revenue-graph.md` — Living network of revenue data; auto-capture and connect every interaction
- `products/engage.md` — Sales engagement and pipeline motion; full context, AI-driven outreach
- `products/forecast.md` — AI-driven pipeline and forecasting; deal risk, paths to target
- `products/agents.md` — AI agents for follow-ups, pipeline edits, enablement, forecast corrections
- `products/collective.md` — 250+ integrations; one platform with CRM and tools

### Personas (5 files)
Load when discussing a specific role or buyer:
- `personas/revenue-leader.md` — CRO / revenue executive; hit the number, align GTM
- `personas/revenue-operations.md` — RevOps; single source of truth, automate workflows
- `personas/sales.md` — Sales teams, leaders, SDRs/BDRs, AEs; productivity, forecast, coaching
- `personas/customer-success.md` — CS leaders and CSMs; retain, expand, ramp, risk visibility
- `personas/enablement.md` — Enablement leaders; prove impact, ramp, execution data

### Pain Points (5 files)
Load when uncovering or addressing pains:
- `pain-points/revenue-leader-pain-points.md` — Forecast surprises, silos, admin, churn risk late
- `pain-points/revenue-operations-pain-points.md` — Fragmented data, reactive vs strategic, prove impact
- `pain-points/sales-pain-points.md` — Admin overload, blind to signals, guesswork coaching, risk late
- `pain-points/customer-success-pain-points.md` — Chasing context, renewal risk late, long ramp, sales–CS disconnect
- `pain-points/enablement-pain-points.md` — Prove impact, learning vs landing, ramp, manager coaching

### Value Propositions (6 files)
Load when crafting messaging or responding to “why Gong”:
- `value-propositions/platform-value-prop.md` — Generic “why Gong”; productivity, predictability, growth
- `value-propositions/revenue-leader-value-prop.md` — CRO; hit the number, visibility, alignment
- `value-propositions/revenue-operations-value-prop.md` — RevOps; single source of truth, strategic
- `value-propositions/sales-value-prop.md` — Sales; better data, less admin, coach to what wins
- `value-propositions/customer-success-value-prop.md` — CS; retain/expand, risk early, ramp
- `value-propositions/enablement-value-prop.md` — Enablement; prove impact, ramp, managers multiply

### Use Cases (5 files)
Load when discussing a scenario or “when would we use Gong”:
- `use-cases/predictable-forecast-pipeline-visibility.md` — One place for number and pipeline; conversation-backed
- `use-cases/scale-rep-productivity-without-headcount.md` — More pipeline from same team; auto-capture, agents
- `use-cases/align-gtm-one-platform.md` — Sales, CS, enablement, RevOps on one platform
- `use-cases/reduce-churn-expand-accounts.md` — CS visibility, risk early, ramp, one account story
- `use-cases/ramp-reps-prove-enablement-impact.md` — Ramp faster; tie enablement to win rate and velocity

### Competitors (3 files)
Load when competing or displacing:
- `competitors/salesloft.md` — Revenue orchestration; Cadence, Conversations, Drift; Gong wins on data layer
- `competitors/outreach.md` — Sales execution; sequences; Gong wins on intelligence and Revenue Graph
- `competitors/clari.md` — RevOps and forecast; Gong wins on conversation-backed forecast and full OS

### Objections (6 files)
Load when handling objections:
- `objections/common-objections.md` — Price, timing, competition, status quo, authority, consolidation
- `objections/revenue-leader-objections.md` — Board/finance, reorg, competition, forecast/CI, alignment
- `objections/revenue-operations-objections.md` — Too many tools, integrations, Salesloft/Clari, data/BI
- `objections/sales-objections.md` — Adoption, cost per seat, competition, status quo
- `objections/customer-success-objections.md` — CS platform, adoption, budget, “sales first”
- `objections/enablement-objections.md` — Prove ROI, LMS, budget, managers’ time

### Case Studies (5 files)
Load when proof or reference is needed:
- `case-studies/frontify.md` — 30% lead conversion; consolidation; RevOps alignment
- `case-studies/crayon.md` — Forecast ownership, accountability, transparency
- `case-studies/uber-for-business.md` — 6,700 hours saved; 32% buyer response lift
- `case-studies/iron-mountain.md` — Onboarding cut in half; enablement impact
- `case-studies/customer-success-ramp.md` — CSM ramp 6 months → ~2 months (Vaishali Reed)

### Sales Plays (4 files)
Load when executing a play or planning outreach:
- `sales-plays/forecast-accuracy-play.md` — Trigger: missed quarter, one source of truth; CRO, RevOps
- `sales-plays/rep-productivity-play.md` — Trigger: more pipeline, admin burden; Sales, RevOps
- `sales-plays/gtm-alignment-play.md` — Trigger: consolidation, reorg; CRO, RevOps
- `sales-plays/enablement-impact-play.md` — Trigger: prove enablement ROI, ramp; Enablement, Sales

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
| Revenue Graph, single source of truth | products/revenue-graph.md, company.md |
| Forecast, pipeline visibility | products/forecast.md, use-cases/predictable-forecast-pipeline-visibility.md |
| Rep productivity, admin, agents | products/agents.md, products/engage.md, use-cases/scale-rep-productivity-without-headcount.md |
| GTM alignment, consolidation | use-cases/align-gtm-one-platform.md, value-propositions/revenue-operations-value-prop.md |
| CS, churn, ramp | personas/customer-success.md, use-cases/reduce-churn-expand-accounts.md |
| Enablement, ramp, prove impact | personas/enablement.md, use-cases/ramp-reps-prove-enablement-impact.md |
| Salesloft / Outreach / Clari | competitors/salesloft.md, competitors/outreach.md, competitors/clari.md |
| Price, timing, competition objections | objections/common-objections.md |
| Frontify, Crayon, Uber, Iron Mountain | case-studies/ |

---
*Last updated: 2026-02-03*
*Generated by Sales Brain*
