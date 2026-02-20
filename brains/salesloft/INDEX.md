# Salesloft Sales Brain Index

## Quick Reference
- **Company**: Salesloft
- **Website**: https://www.salesloft.com/
- **Positioning**: Leading AI Revenue Orchestration Platform — put your wins on repeat; smarter execution, more qualified pipeline, faster deal cycles
- **Main Products**: Cadence, Rhythm, Conversations, Deals, Forecast, Drift, Analytics, AI Agents

## Available Context Files

### Always Relevant
- `company.md` — Company overview, positioning, target market, differentiators, proof points
- `target-companies.md` — Target customer profiles (industries, roles, use cases); named proof points (3M, Wrike, NFP)

### Products (8 files)
Load when user asks about a specific product or capability:
- `products/cadence.md` — Sales engagement, pipeline, nurture; Account Agents, Focus Zone, dialer, calendaring
- `products/rhythm.md` — Prioritization, Signals, Plays, Focus Zones; right actions at the right moments
- `products/deals.md` — Deal management, Close Focus Zone, buying group, MEDDPICC, forecast integration
- `products/conversations.md` — Conversation intelligence; scorecards, key moments, summaries, action items
- `products/drift.md` — Website chat and conversion; AI agents, Live Chat, Fastlane, ROI reporting
- `products/forecast.md` — AI forecasting; real-time deal data, strategic action plan
- `products/analytics.md` — Centralized reporting, performance insights, Analytics Interpreter
- `products/ai-agents.md` — Purpose-built agents (research, email, prioritization, summaries, deal/forecast, custom)

### Personas (6 files)
Load when discussing a specific role or buyer:
- `personas/revenue-operations.md` — RevOps; align teams, consolidate stack, govern GTM
- `personas/sales-leader.md` — VP Sales, Director; coach, forecast, pipeline visibility
- `personas/sales-development.md` — SDR/BDR; pipeline creation, prioritization, conversion
- `personas/account-executive.md` — AEs, front line sellers; close faster, Rhythm, Deals, Mobile
- `personas/marketing.md` — Marketing; Drift, website conversion, align with sales
- `personas/customer-success.md` — CS; retain, expand, churn, renewals, cadences

### Pain Points (4 files)
Load when uncovering or addressing pains:
- `pain-points/sales-pain-points.md` — Prospecting, admin, focus, pipeline/forecast visibility, coaching
- `pain-points/revenue-operations-pain-points.md` — Scattered data, visibility, forecast, workflows, governance
- `pain-points/marketing-pain-points.md` — Website conversion, intent visibility, handoff, alignment
- `pain-points/customer-success-pain-points.md` — Churn, engagement, growth visibility, renewals, health view

### Value Propositions (5 files)
Load when crafting messaging or responding to "why Salesloft":
- `value-propositions/platform-value-prop.md` — Full platform; put your wins on repeat; 10-day value; 3M, Wrike, NFP
- `value-propositions/sales-value-prop.md` — Sales; pipeline, cut busywork, coach to close; Beam, Forrester TEI
- `value-propositions/revenue-operations-value-prop.md` — RevOps; align, consolidate, govern; Wrike visibility, $350k
- `value-propositions/marketing-value-prop.md` — Marketing; Drift, pipeline goals, align sales and marketing
- `value-propositions/customer-success-value-prop.md` — CS; deliver value, loyalty, churn, renewals, scale touchpoints

### Use Cases (5 files)
Load when discussing a scenario or "when would we use Salesloft":
- `use-cases/pipeline-creation-coverage.md` — Transform prospects into pipeline; 254%, 60%, 50% (Forrester); Cadence, Rhythm
- `use-cases/team-productivity-performance.md` — Efficiency and effectiveness; pipeline review half (Beam); Rhythm, AI agents
- `use-cases/opportunity-acceleration-management.md` — Close faster; 3M 2.5x; Deals, Rhythm, Conversations, Forecast
- `use-cases/customer-loyalty-growth.md` — Retain, expand, churn, renewals; Cadence, Deals, Forecast
- `use-cases/technology-workflow-optimization.md` — Consolidate stack; Wrike $350k, 3M one-stop-shop; one platform

### Competitors (2 files)
Load when competing or displacing:
- `competitors/gong.md` — Revenue AI OS, Revenue Graph; Salesloft wins on Drift, 10-day value, one workflow
- `competitors/outreach.md` — AI Revenue Workflow; Salesloft wins on Drift, 10-day value, Rhythm/Conversations in workflow

### Objections (3 files)
Load when handling objections:
- `objections/common-objections.md` — Price, timing, competition (Gong/Outreach), status quo, authority
- `objections/sales-objections.md` — Adoption, already have outreach, pipeline review fine, ROI, forecast separate
- `objections/revenue-operations-objections.md` — Consolidation, visibility, governance, implementation, evaluating Gong/Outreach

### Case Studies (4 files)
Load when proof or reference is needed:
- `case-studies/3m.md` — 2.5x faster close; one-stop-shop platform
- `case-studies/wrike.md` — $350k savings, visibility, operational soulmate
- `case-studies/nfp.md` — Over $1M revenue; reverse-engineer activities for pipeline goals
- `case-studies/beam.md` — Pipeline review cut by half; much tighter forecast

### Sales Plays (3 files)
Load when executing a play or planning outreach:
- `sales-plays/competitive-displacement.md` — vs. Gong/Outreach; Drift, 10-day value, one workflow
- `sales-plays/platform-consolidation-play.md` — RevOps; one platform; Wrike, 3M proof
- `sales-plays/new-sales-leader-play.md` — New sales leader; pipeline/forecast visibility; Beam, 3M

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
| Cadence, pipeline, engagement | products/cadence.md, use-cases/pipeline-creation-coverage.md |
| Rhythm, prioritization, Focus Zones | products/rhythm.md, personas/account-executive.md |
| Deals, forecast visibility | products/deals.md, products/forecast.md, use-cases/opportunity-acceleration-management.md |
| Conversations, coaching | products/conversations.md, personas/sales-leader.md |
| Drift, website conversion | products/drift.md, personas/marketing.md, value-propositions/marketing-value-prop.md |
| AI agents | products/ai-agents.md |
| Consolidation, RevOps | use-cases/technology-workflow-optimization.md, value-propositions/revenue-operations-value-prop.md, case-studies/wrike.md |
| 10-day time to value | company.md, value-propositions/platform-value-prop.md |
| Gong / Outreach | competitors/gong.md, competitors/outreach.md |
| 3M, Wrike, NFP, Beam | case-studies/3m.md, case-studies/wrike.md, case-studies/nfp.md, case-studies/beam.md |

---
*Last updated: 2026-02-03*
*Generated by Sales Brain*

## V1 Loading Note

- Prefer files with complete `Evidence & Sources` entries.
- Treat `To be verified` claims as hypotheses, not final proof.
