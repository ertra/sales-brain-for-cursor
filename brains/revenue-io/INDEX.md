# Revenue.io Sales Brain Index

## Quick Reference
- **Company**: Revenue.io (formerly ringDNA)
- **Website**: https://www.revenue.io/
- **Positioning**: The #1 Revenue Orchestration Platform for Salesforce—dialer, engagement, conversation AI, real-time in-call guidance (Moments), rep coaching, and forecasting in one platform
- **Main Products**: Revenue Platform, Salesforce Dialer (RingDNA), Guided Selling, Conversation AI, Moments, Deal Execution, AI Agents, Rep Coaching, Sales Forecasting, Lead Response, CallerDNA

## Available Context Files

### Always Relevant
- `company.md` — Company overview, mission, target market, differentiators, compliance
- `target-companies.md` — Target segments (enterprise, mid-market, Salesforce-centric, by role, by industry)

### Products (11 files)
Load when user asks about a specific product or capability:
- `products/revenue-platform.md` — Unified Salesforce-native platform; dialer, engagement, CI, guidance, forecasting
- `products/salesforce-dialer.md` — #1 Salesforce-native dialer (RingDNA)
- `products/guided-selling.md` — Sales engagement; cadences, email automation, prioritization
- `products/conversation-ai.md` — Conversation intelligence; recording, transcripts, summaries, scorecards
- `products/moments.md` — Real-time in-call guidance
- `products/callerdna.md` — Call tracking, routing, attribution
- `products/deal-execution.md` — Opportunity summaries, deal scorecards, forecast
- `products/ai-agents.md` — AI agents; Ask Revenue AI
- `products/rep-coaching.md` — AI feedback, scorecards, performance analytics
- `products/sales-forecasting.md` — Deal health, forecast analyzer
- `products/lead-response.md` — Hot Leads, instant lead response

### Personas (8 files)
Load when discussing a specific role or buyer:
- `personas/sales-leader.md` — VP Sales, Director; forecast, coaching, pipeline, consolidate stack
- `personas/account-executive.md` — AE; less manual work, close faster, in-call guidance
- `personas/revenue-operations.md` — RevOps; automate workflows, consolidate stack, clean Salesforce
- `personas/sales-development.md` — SDR/BDR; connect faster, automate follow-ups, real-time guidance
- `personas/enablement.md` — Enablement; scale coaching, ramp time, measure impact
- `personas/customer-success.md` — CS; see risk early, account health, expansion
- `personas/marketer.md` — Marketer; campaigns to revenue, lead response, full-funnel visibility
- `personas/customer-support.md` — Support; faster resolution, first-call resolution, real-time coaching

### Pain Points (8 files)
Load when uncovering or addressing pains:
- `pain-points/sales-leader-pain-points.md` — Post-hoc coaching, forecast accuracy, tool sprawl
- `pain-points/account-executive-pain-points.md` — Manual work, no in-call guidance, unclear deal health
- `pain-points/revenue-operations-pain-points.md` — Disconnected tools, multiple vendors, no attribution
- `pain-points/sales-development-pain-points.md` — Slow connection, manual follow-up, no in-call guidance
- `pain-points/enablement-pain-points.md` — Coaching doesn't scale, can't measure impact, slow ramp
- `pain-points/customer-success-pain-points.md` — Reacting to churn, no single view, can't prove value
- `pain-points/marketer-pain-points.md` — Can't tie campaigns to revenue, slow lead response
- `pain-points/customer-support-pain-points.md` — Slow resolutions, inconsistent performance, high escalations

### Value Propositions (6 files)
Load when crafting messaging or "why Revenue.io":
- `value-propositions/revenue-platform-sales-leader.md` — One platform; 120% quota, $300K rep productivity, 60% ramp; HPE, NFI
- `value-propositions/moments-account-executive.md` — Live in-call guidance; close with confidence
- `value-propositions/salesforce-dialer-sales-development.md` — #1 dialer; 10x meetings (NFI), 400% opportunities (HPE)
- `value-propositions/revenue-platform-revenue-operations.md` — One platform; consolidate stack, clean Salesforce
- `value-propositions/rep-coaching-enablement.md` — Scale coaching; 60% ramp reduction; measure impact
- `value-propositions/lead-response-marketer.md` — Instant lead response; connect campaigns to revenue

### Use Cases (5 files)
Load when discussing a scenario or "when would we use Revenue.io":
- `use-cases/scale-pipeline-and-meetings.md` — 400% opportunities (HPE), 10x meetings (NFI), Vagaro
- `use-cases/improve-quota-attainment-and-forecast.md` — 120% quota, Vagaro 400%, Jan Dils
- `use-cases/scale-coaching-and-reduce-ramp-time.md` — 60% ramp; OrthoFX 60% productivity; NFI, HireRight
- `use-cases/respond-to-leads-instantly.md` — Vagaro 48h→3.5min, RE/MAX 100% capture
- `use-cases/consolidate-revenue-stack-salesforce.md` — Fundera, OrthoFX, Nutanix; one platform

### Competitors (3 files)
Load when competing or displacing:
- `competitors/gong.md` — Revenue AI OS; Revenue.io wins on Salesforce-native, #1 dialer, Moments (in-call)
- `competitors/outreach.md` — AI Revenue Workflow; Revenue.io wins on dialer in platform, Moments
- `competitors/salesloft.md` — AI Revenue Orchestration; Revenue.io wins on #1 dialer built in, Moments

### Objections (4 files)
Load when handling objections:
- `objections/common-objections.md` — Salesforce-only, price, timing, competition, status quo, authority, real-time, implementation
- `objections/sales-leader-objections.md` — Gong/Outreach, cost, timing, adoption, proof
- `objections/revenue-operations-objections.md` — Happy with dialer, customized Salesforce, security, Gong/Outreach, implementation
- `objections/account-executive-objections.md` — Another tool, real-time listening, already doing fine, slow down, Gong/Outreach

### Case Studies (5 files)
Load when proof or reference is needed:
- `case-studies/hewlett-packard-enterprise.md` — 400% more opportunities; 100% adoption; global 150+ countries
- `case-studies/nutanix.md` — 2+ hours saved per rep; live coaching from anywhere
- `case-studies/orthofx.md` — 60% productivity; 20%+ MoM conversions; only platform that met requirements
- `case-studies/freshbooks.md` — 90–100 calls/day; 11%→21% pickup; best sales productivity investment
- `case-studies/nfi-industries.md` — 10x meetings; 8x conversations; seven-figure rep story

### Sales Plays (3 files)
Load when executing a play or planning outreach:
- `sales-plays/consolidation-play.md` — Replace dialer + Gong/Outreach/Salesloft; Sales Leader, RevOps
- `sales-plays/real-time-coaching-play.md` — Moments + Rep Coaching; scale coaching, 60% ramp
- `sales-plays/scale-meetings-global-inside-sales-play.md` — HPE 400%, NFI 10x; global inside sales

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
| Revenue platform, one platform | company.md, products/revenue-platform.md |
| Salesforce dialer, RingDNA | products/salesforce-dialer.md, value-propositions/salesforce-dialer-sales-development.md |
| Real-time guidance, Moments | products/moments.md, value-propositions/moments-account-executive.md |
| Conversation AI, coaching | products/conversation-ai.md, products/rep-coaching.md |
| Consolidation, replace Gong/Outreach/Salesloft | use-cases/consolidate-revenue-stack-salesforce.md, sales-plays/consolidation-play.md |
| Scale meetings, 400%, 10x | use-cases/scale-pipeline-and-meetings.md, case-studies/hewlett-packard-enterprise.md, case-studies/nfi-industries.md |
| Lead response, speed-to-lead | use-cases/respond-to-leads-instantly.md, value-propositions/lead-response-marketer.md |
| HPE, NFI, Fundera, OrthoFX | case-studies/ |
| Gong / Outreach / Salesloft | competitors/ |

---
*Last updated: 2026-02-08*
*Generated by Sales Brain*

## V1 Loading Note

- Prefer files with complete `Evidence & Sources` entries.
- Treat `To be verified` claims as hypotheses, not final proof.
