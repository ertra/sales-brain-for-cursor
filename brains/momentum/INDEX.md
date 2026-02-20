# Momentum Sales Brain Index

## Quick Reference
- **Company**: Momentum
- **Website**: https://www.momentum.io/
- **Positioning**: AI Revenue Orchestration Platform — Your Revenue Engine Supercharged. First Call to Renewals. (Definitive agreement to be acquired by Salesforce.)
- **Main Products**: Deal Execution Agent, Customer Retention Agent, Coaching Agent, AI CRO; SmartClips, Deep Research, Integrations (Salesforce, Slack, Teams coming, Snowflake)

## Available Context Files

### Always Relevant
- `company.md` — Company overview, positioning, target market, differentiators, proof points
- `target-companies.md` — Target customer profiles (Enterprise GTM, Technology/SaaS, RevOps, Sales, CS, CRO); named proof points

### Products (6 files)
Load when user asks about a specific product or capability:
- `products/platform-overview.md` — AI Revenue Orchestration; four agents; solutions by role
- `products/deal-execution-agent.md` — Auto notes, CRM writeback, MEDDIC Autopilot, prep + follow-up in Slack
- `products/customer-retention-agent.md` — Churn risk, sentiment, cases in Salesforce, Slack alerts
- `products/coaching-agent.md` — AI sales coaching, SmartClips, scorecards, compliance
- `products/ai-cro.md` — CRO briefs, Ask Momentum, closed/lost analysis, pipeline/team visibility
- `products/platform-overview.md` — Cross-cutting: SmartClips, Deep Research, Integrations

### Personas (10 files)
Load when discussing a specific role or buyer:
- `personas/cro.md` — CRO; visibility, forecast, closed/lost
- `personas/revops.md` — RevOps; CRM hygiene, forecast, fits process
- `personas/sales-manager.md` — Front Line Sales Leader; pipeline, coaching, handoffs
- `personas/sales-rep.md` — AE; more time selling, auto notes/follow-up
- `personas/sdr-bdr.md` — BDR/SDR; prep, compliance, handoff, coaching
- `personas/customer-success-leader.md` — CS Leader; churn risk, handoff
- `personas/customer-success-manager.md` — CSM; notes/cases, churn alerts
- `personas/enablement.md` — Enablement; feedback loop, SmartClips, ramp
- `personas/marketing-leader.md` — Marketing; market research, case study candidates
- `personas/product-team-leader.md` — Product; feedback, win/loss, signals

### Pain Points (6 files)
Load when uncovering or addressing pains:
- `pain-points/sales-pain-points.md` — Admin, visibility chasing, forecast guesswork, coaching scale, handoffs
- `pain-points/revops-pain-points.md` — Reps don't update CRM, forecast guesswork, tool fatigue, flexibility
- `pain-points/customer-success-pain-points.md` — Churn late, manual notes/cases, handoff, sentiment view
- `pain-points/revenue-leader-pain-points.md` — Scattered truth, gut forecast, churn late, chasing clarity
- `pain-points/enablement-pain-points.md` — Trends late, blindspots, ramp, coachable moments, compliance
- `pain-points/marketing-pain-points.md` — Insights trapped, case study candidates, campaign disconnect

### Value Propositions (6 files)
Load when crafting messaging or "why Momentum":
- `value-propositions/deal-execution-agent-sales.md` — Sales; cut time in half, lead with visibility
- `value-propositions/deal-execution-agent-revops.md` — RevOps; CRM clean, forecast confidence, fits process
- `value-propositions/customer-retention-agent-customer-success.md` — CS; churn real time, save accounts
- `value-propositions/coaching-agent-sales-leader.md` — Sales Leader; data-backed coaching, ramp cut
- `value-propositions/coaching-agent-enablement.md` — Enablement; live feedback loop, SmartClips
- `value-propositions/ai-cro-revenue-leader.md` — CRO; cappuccino updates, order of magnitude data

### Use Cases (5 files)
Load when discussing a scenario or "when would we use Momentum":
- `use-cases/scale-rep-productivity-deal-execution.md` — Cut time in half; one source of truth; Ramp, 1Password
- `use-cases/flag-churn-retain-customers.md` — Churn risk real time; save critical accounts; Demandbase
- `use-cases/coach-at-scale-cut-ramp.md` — Data-backed coaching; SmartClips; ramp cut in half
- `use-cases/forecast-executive-visibility.md` — AI CRO; order of magnitude data; Owner, Dealfront
- `use-cases/democratized-gtm-data-one-source.md` — One sheet of paper; Ramp, Snorkel, Demandbase

### Competitors (3 files)
Load when competing or displacing:
- `competitors/gong.md` — Revenue AI OS; Momentum wins on Slack + write to Salesforce, fits process
- `competitors/clari.md` — Revenue platform, forecast; Momentum wins on conversation-backed data, writeback
- `competitors/salesloft.md` — AI Revenue Orchestration; Momentum wins on Slack command center, writeback

### Objections (3 files)
Load when handling objections:
- `objections/common-objections.md` — Price, timing, competition (Gong/Clari/Salesloft), status quo, another tool, security, acquisition
- `objections/revops-objections.md` — Already have Gong/Clari, adoption, flexibility, data quality, fill gap
- `objections/sales-leader-objections.md` — Reps won't use, visibility, coaching scale, handoffs, forecast real

### Case Studies (4 files)
Load when proof or reference is needed:
- `case-studies/ramp.md` — Cut time in half; one source of truth; clarity; RevOps + GTM
- `case-studies/1password.md` — Insight at scale; reps spending time selling
- `case-studies/owner.md` — Order of magnitude better data; coaching 24/7
- `case-studies/demandbase.md` — Save critical accounts; analysts not curating hours

### Sales Plays (3 files)
Load when executing a play or planning outreach:
- `sales-plays/deal-execution-slack-command-center.md` — Deal execution + Slack; cut time in half; RevOps, Sales Leader
- `sales-plays/executive-visibility-order-of-magnitude-data.md` — CRO visibility; order of magnitude data
- `sales-plays/churn-risk-save-critical-accounts.md` — Churn real time; save critical accounts; CS

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
| Deal execution, cut time in half, write to Salesforce | products/deal-execution-agent.md, value-propositions/deal-execution-agent-sales.md, case-studies/ramp.md |
| Slack as command center, 24/7 sales manager | company.md, use-cases/scale-rep-productivity-deal-execution.md, sales-plays/deal-execution-slack-command-center.md |
| RevOps, CRM hygiene, fits process | personas/revops.md, value-propositions/deal-execution-agent-revops.md, objections/revops-objections.md |
| Churn risk, save critical accounts, CS | products/customer-retention-agent.md, use-cases/flag-churn-retain-customers.md, case-studies/demandbase.md |
| Coaching, SmartClips, ramp | products/coaching-agent.md, value-propositions/coaching-agent-sales-leader.md, use-cases/coach-at-scale-cut-ramp.md |
| AI CRO, executive visibility, order of magnitude data | products/ai-cro.md, value-propositions/ai-cro-revenue-leader.md, case-studies/owner.md |
| One source of truth, democratized GTM data | use-cases/democratized-gtm-data-one-source.md, target-companies.md |
| Gong / Clari / Salesloft | competitors/gong.md, competitors/clari.md, competitors/salesloft.md |
| Price, timing, competition, acquisition objections | objections/common-objections.md |

---
*Last updated: 2026-02-19*
*Generated by Sales Brain*

## V1 Loading Note

- Prefer files with complete `Evidence & Sources` entries.
- Treat `To be verified` claims as hypotheses, not final proof.
