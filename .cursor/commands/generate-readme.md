# Generate README

Generate or regenerate the README.md file for a company's Sales Brain folder. GitHub (and other tools) show README.md by default when viewing a directory, so this gives the company folder a clear, human-readable overview.

## Usage

```
/generate-readme {company}
```

**Examples:**
- `/generate-readme lautie` - Generate README for Lautie
- `/generate-readme outreach` - Generate README for Outreach

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /generate-readme {company}

Example: /generate-readme lautie
```

## What It Does

Creates or updates `brains/{company}/README.md` with:

1. **Company name and tagline** – From company.md (Overview, Mission/Vision, Tagline)
2. **Short summary** – 2–4 sentences about the company and what this folder contains
3. **Website** – Link to company URL
4. **What’s in this folder** – Brief description of the Sales Brain structure (products, personas, use cases, competitors, objections, case studies, sales plays)
5. **Quick links** – Table or list of main files/sections (company.md, INDEX.md, products/, personas/, etc.)
6. **How to use** – One or two lines on using README.md for overview and INDEX.md for full file list
7. **Optional** – Key differentiators, target segments, or product lines in compact form (if space allows)
8. **V2 note** – Include a short note when folder content is partially or fully migrated to V2 template contract

The README should be **human-friendly** so that anyone opening the folder on GitHub or in a file browser gets a clear overview.

## Workflow Steps

1. **Verify company exists**
   - Check if `brains/{company}/` directory exists
   - If not: tell user to run `/start` or specify a valid company name

2. **Gather content**
   - Read `brains/{company}/company.md` for name, overview, website, tagline, differentiators
   - Optionally list directories under `brains/{company}/` (products/, personas/, etc.) and count or list key files

3. **Generate README.md**

Use this template structure (adapt to what exists):

```markdown
# {Company Display Name}

{Optional tagline from company.md}

## About

{2–4 sentence summary of the company, from company.md Overview. Then one sentence: "This folder contains the Sales Brain for {Company}: structured sales and product context used for AI-assisted research and outreach."}

**Website:** [{URL}]({URL})

## What’s in this folder

| Section | Description |
|--------|-------------|
| `company.md` | Company overview, mission, differentiators |
| `target-companies.md` | Target customers / segments |
| `INDEX.md` | Full file inventory and loading rules |
| `products/` | Product or product-line descriptions |
| `personas/` | Buyer or user personas |
| `pain-points/` | Pain points by persona |
| `value-propositions/` | Value props and messaging |
| `use-cases/` | Use cases and scenarios |
| `competitors/` | Competitive battlecards |
| `objections/` | Objection handling |
| `case-studies/` | Customer or composite stories |
| `sales-plays/` | Sales plays and triggers |

{Omit rows for sections that don’t exist.}

## Quick start

- **Overview:** This README is the one-page overview of the folder.
- **Full map:** Open `INDEX.md` for the complete file list and topic mapping.

{Optional: 1–2 sentences on key differentiators or target segments from company.md.}
```

4. **Write the file**
   - Save to `brains/{company}/README.md`

5. **Confirm**
   - Tell the user the README was created/updated and where it is

## When to Run

- After completing the Sales Brain workflow for a new company (e.g. after Phase 11 or after generating INDEX/SUMMARY)
- After major changes to company.md or structure
- Manually anytime with `/generate-readme {company}`

## Output Example

```
✅ Generated README.md for Lautie

README includes:
- Company name and summary
- Website link
- Table of contents (company.md, INDEX.md, products/, personas/, …)
- Quick start (this README and INDEX.md)

Location: lautie/README.md
```

## Error Handling

- **Company folder missing:** Tell user "Company '{company}' not found. Use `/start` to create a company or specify an existing company name (companies live under brains/)."
- **company.md missing:** Still generate README with placeholder text for company name/summary and note that company.md is missing.
- **Empty or missing sections:** Omit those rows from the "What's in this folder" table; only list sections that exist.
