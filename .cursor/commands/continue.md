# Continue Sales Brain Workflow

Continue the Sales Brain workflow for a specific company from where it left off.

## Required Parameter

**This command requires a company name parameter.**

If the user runs `/continue` without a company name:
- ❌ Do NOT proceed with the workflow
- Tell the user: "Please specify the company name. Usage: `/continue {company-name}`"
- List available company directories if any exist

**Examples:**
- ✅ `/continue outreach` - Continue workflow for Outreach
- ✅ `/continue gong` - Continue workflow for Gong
- ❌ `/continue` - Missing company name, show error

## How to Continue

When a valid company name is provided:

### Step 1: Verify Company Directory Exists

Check if `brains/{company-slug}/` directory exists.

If it doesn't exist:
- Tell user: "Company '{company}' not found. Available companies: [list from brains/]. Or use `/start` to begin a new company."

### Step 2: Detect Completed Phases

Check which files/directories exist to determine progress:

| Phase | Check | Files to Look For |
|-------|-------|-------------------|
| 1. Company | ✓ if exists | `brains/{company}/company.md` |
| 2. Products | ✓ if has files | `brains/{company}/products/*.md` |
| 3. Target Companies | ✓ if exists | `brains/{company}/target-companies.md` |
| 4. Personas | ✓ if has files | `brains/{company}/personas/*.md` |
| 5. Pain Points | ✓ if has files | `brains/{company}/pain-points/*.md` |
| 6. Value Props | ✓ if has files | `brains/{company}/value-propositions/*.md` |
| 7. Use Cases | ✓ if has files | `brains/{company}/use-cases/*.md` |
| 8. Competitors | ✓ if has files | `brains/{company}/competitors/*.md` |
| 9. Objections | ✓ if has files | `brains/{company}/objections/*.md` |
| 10. Case Studies | ✓ if has files | `brains/{company}/case-studies/*.md` |
| 11. Sales Plays | ✓ if has files | `brains/{company}/sales-plays/*.md` |

### Step 3: Show Progress Summary

Display to user:
```
🧠 Sales Brain - Continuing {Company Name}

Progress:
✅ Phase 1: Company Research - company.md exists
✅ Phase 2: Products - 5 products found
✅ Phase 3: Target Companies - target-companies.md exists
⏳ Phase 4: Personas - Not started
⬚ Phase 5: Pain Points
⬚ Phase 6: Value Propositions
⬚ Phase 7: Use Cases
⬚ Phase 8: Competitors
⬚ Phase 9: Objections
⬚ Phase 10: Case Studies
⬚ Phase 11: Sales Plays

Next: Phase 4 - Persona Research
```

### Step 4: Ask User to Confirm

Ask: "Ready to continue with Phase {X}: {Phase Name}? (yes/no)"

Or offer options:
- "Continue with Phase {X}"
- "Skip to a different phase"
- "Review completed phases first"

### Step 5: Execute the Phase

Run the appropriate phase using the workflow from `.cursor/rules/workflow/RULE.md`.

Remember to use Python scraping:
```bash
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url>
```

## Error Messages

### No company parameter
```
❌ Please specify the company name.

Usage: /continue {company-name}

Example: /continue outreach
```

### Company not found
```
❌ Company '{company}' not found.

Available companies (from brains/):
- outreach
- gong

Or use /start to begin a new company.
```
(List available companies by listing subdirectories of `brains/`.)

### All phases complete
```
✅ All 11 phases are complete for {Company}!

You can:
- Use /add commands to add more objects
- Use /update commands to refresh information
- Use /start to begin a new company
```

## Phase Execution Reference

When continuing a phase, follow the workflow in `.cursor/rules/workflow/RULE.md`:

- **Phase 4 (Personas)**: Scrape solutions pages, ask user for personas
- **Phase 5 (Pain Points)**: Scrape G2 reviews, document pain points
- **Phase 6 (Value Props)**: Scrape value pages, map products to personas
- **Phase 7 (Use Cases)**: Scrape case studies, create use case files
- **Phase 8 (Competitors)**: Scrape competitor websites directly
- **Phase 9 (Objections)**: Scrape reviews/FAQs, document objections
- **Phase 10 (Case Studies)**: Scrape customer stories
- **Phase 11 (Sales Plays)**: Synthesize into playbooks
