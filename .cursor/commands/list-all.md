# List All Sales Objects

List all sales objects for a specific company or show all companies.

## Usage

```
/list all                  # Show all companies
/list all {company}        # Show all objects for a company
```

**Examples:**
- `/list all` - Show all tracked companies
- `/list all outreach` - Show all Outreach sales objects

## Workflow

### If no company specified: Show all companies

```
🧠 Sales Brain - All Companies

Found 2 company directories:

1. outreach/
   - Products: 7
   - Personas: 6
   - Competitors: 3
   - Status: 11/11 phases complete

2. gong/
   - Products: 5
   - Personas: 3
   - Status: 4/11 phases complete

Use /list all {company} for details.
```

### If company specified: Show all objects

```
🧠 Sales Brain - Outreach (Complete)

## Foundation
- Company: ✅ company.md
- Products: 7 files
  - sales-engagement.md
  - ai-agents.md
  - conversation-intelligence.md
  - sales-forecasting.md
  - deal-management.md
  - mutual-action-plans.md
  - rep-coaching.md
- Target Companies: ✅ target-companies.md

## Who We Sell To
- Personas: 6 files
  - sdr-bdr.md
  - account-executive.md
  - sales-manager.md
  - vp-of-sales.md
  - revenue-operations.md
  - cro.md

## Why They Buy
- Pain Points: 6 files
- Value Propositions: 7 files
- Use Cases: 4 files

## How We Win
- Competitors: 3 files (gong, salesloft, clari)
- Objections: 6 files
- Case Studies: 5 files
- Sales Plays: 4 files

## Statistics
- Total files: 54
- All phases: Complete ✅
- Last updated: Today
```

## Company Not Found

```
❌ Company '{company}' not found.

Available companies:
- outreach
- gong

Use /start to begin a new company.
```
