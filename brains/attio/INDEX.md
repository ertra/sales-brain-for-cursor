# Attio Sales Brain Index

## Quick Reference
- **Company**: Attio
- **Website**: https://attio.com
- **Positioning**: The AI CRM for GTM — "Ask more from CRM. Ask Attio." Flexible data model, workflows, Ask Attio (AI), reporting, and data sync in one platform; from zero to IPO.
- **Main Products**: Platform (Free/Plus/Pro/Enterprise), Ask Attio, Workflows & Automations, Data model & syncing, Reporting

## Available Context Files

### Always Relevant
- `company.md` — Company overview, mission, target market, differentiators, funding
- `target-companies.md` — Target segments (startups, scale-ups, enterprise, PLG/PLS, investors)

### Products (5 files)
Load when user asks about a specific product or capability:
- `products/platform.md` — Core platform; pricing (Free, Plus, Pro, Enterprise); GTM at full throttle
- `products/ask-attio.md` — AI: meeting prep, deal brief, Universal Context; real information, permissions
- `products/automations.md` — Workflows, sequences, AI blocks; integrations (Slack, Typeform, Outreach, webhooks)
- `products/data.md` — Data model, custom objects, enrichment, sync (warehouses, email/calendar)
- `products/reporting.md` — Real-time reporting, dashboards, group your way, historical

### Personas (6 files)
Load when discussing a specific role or buyer:
- `personas/sales-rep.md` — AE, SDR, BDR; pipeline, meeting prep, sequences, Ask Attio
- `personas/revenue-operations.md` — RevOps; data model, workflows, reporting, single source of truth
- `personas/customer-success.md` — CSM; handoffs, health, renewals, QBR prep
- `personas/founder-gtm-leader.md` — Founder, VP GTM, CRO; from zero to IPO, sales + onboarding + CS
- `personas/investor-deal-flow.md` — Investor, deal flow; deal engine, pipeline, Seedcamp/USV
- `personas/marketing.md` — Demand, growth; lead routing, triage, attribution (Granola 83%)

### Pain Points (6 files)
Load when uncovering or addressing pains:
- `pain-points/sales-rep-pain-points.md` — Context scattered, CRM = data entry, CRM doesn't fit motion
- `pain-points/revenue-operations-pain-points.md` — Schema doesn't match business, data silos, automations brittle
- `pain-points/customer-success-pain-points.md` — No single view, manual handoffs, health/renewal scattered
- `pain-points/founder-gtm-leader-pain-points.md` — CRM overcomplicated, need one system, fundraising/recruiting
- `pain-points/investor-deal-flow-pain-points.md` — Deals in spreadsheets, siloed data, reporting doesn't scale
- `pain-points/marketing-pain-points.md` — Lead data disconnected, manual triage, attribution exports

### Value Propositions (6 files)
Load when crafting messaging or "why Attio":
- `value-propositions/sales-rep-value-prop.md` — Prep for every call; update deals in seconds; CRM that fits
- `value-propositions/revenue-operations-value-prop.md` — Business model in CRM; single source of truth; automate your way
- `value-propositions/customer-success-value-prop.md` — Full context; handoffs; health/renewals in one place
- `value-propositions/founder-gtm-leader-value-prop.md` — From zero to IPO; one GTM engine; sales, fundraising, recruiting
- `value-propositions/investor-deal-flow-value-prop.md` — Deal engine; fragmented to unified; reporting scales
- `value-propositions/marketing-value-prop.md` — Lead data in CRM; 83% faster triage; full-funnel reporting

### Use Cases (5 files)
Load when discussing a scenario or "when would we use Attio":
- `use-cases/product-signals-into-revenue-lead-triage.md` — 83% faster triage; Granola; product + leads in one place
- `use-cases/workflow-automation-plg-at-scale.md` — PLG + workspaces; Modal; single source of truth
- `use-cases/single-source-of-truth-gtm.md` — Flatfile; migrate from Salesforce; lifecycle automated
- `use-cases/deal-flow-at-scale.md` — Investors; Seedcamp, USV; deal engine, unified pipeline
- `use-cases/meeting-prep-context-every-call.md` — Ask Attio; prep, deal brief, update in seconds

### Competitors (3 files)
Load when competing or displacing:
- `competitors/hubspot.md` — Attio wins on PLG, workspaces, flexible data model (Modal left HubSpot)
- `competitors/salesforce.md` — Attio wins on sync, single source of truth, migration speed (Flatfile left Salesforce)
- `competitors/pipedrive.md` — Attio wins on flexibility, Ask Attio, product sync, from zero to IPO

### Objections (4 files)
Load when handling objections:
- `objections/common-objections.md` — Price, timing, competition (SF/HubSpot/Pipedrive), migration, status quo, authority
- `objections/sales-rep-objections.md` — Another tool, process works, AI trust, adoption
- `objections/revenue-operations-objections.md` — Customized SF/HubSpot, migration risk, security, data model complex
- `objections/founder-gtm-leader-objections.md` — Too small, not now, good enough, let team decide

### Case Studies (3 files)
Load when proof or reference is needed:
- `case-studies/granola.md` — 83% faster lead triage; 10x context; 5 hrs/week saved; 100% adoption
- `case-studies/modal.md` — Left HubSpot; native Workspaces; "configure to fit our business"; delight to work in
- `case-studies/flatfile.md` — Left Salesforce; migration ~1 month; "it all just works"; single source of truth

### Sales Plays (3 files)
Load when executing a play or planning outreach:
- `sales-plays/plg-workspaces-vs-hubspot.md` — Win PLG teams on HubSpot; Modal story; Workspaces, Segment
- `sales-plays/single-source-of-truth-vs-salesforce.md` — Migrate from Salesforce; Flatfile story; ~1 month
- `sales-plays/meeting-prep-ask-attio.md` — Meeting prep & context; Ask Attio; Granola, Ian Ahuja

## Loading Rules for AI Agents
- **Company or overview** → `company.md`, `target-companies.md`
- **Product question** → relevant file in `products/`
- **Persona or role** → relevant file in `personas/`, then `pain-points/`, `value-propositions/`, `objections/` for that persona
- **Use case or scenario** → relevant file in `use-cases/`
- **Competitor** → relevant file in `competitors/`
- **Objection** → `objections/common-objections.md` then persona-specific in `objections/`
- **Proof / reference** → relevant file in `case-studies/`
- **Play execution** → relevant file in `sales-plays/`

## File Inventory (Counts)
| Category | Count | Path |
|----------|-------|------|
| Company | 2 | company.md, target-companies.md |
| Products | 5 | products/*.md |
| Personas | 6 | personas/*.md |
| Pain Points | 6 | pain-points/*.md |
| Value Propositions | 6 | value-propositions/*.md |
| Use Cases | 5 | use-cases/*.md |
| Competitors | 3 | competitors/*.md |
| Objections | 4 | objections/*.md |
| Case Studies | 3 | case-studies/*.md |
| Sales Plays | 3 | sales-plays/*.md |
| Scraped data | (JSON) | scraped/*.json |

---
*Last updated: 2026-02-17*  
*Generated by Sales Brain*

## V1 Loading Note

- Prefer files with complete `Evidence & Sources` entries.
- Treat `To be verified` claims as hypotheses, not final proof.
