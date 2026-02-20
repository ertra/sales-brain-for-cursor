# Start Sales Brain Workflow

When the user types `/start`, begin the Sales Brain research workflow.

## Step 0 (Strict): Collect Inputs Before Any Scraping

Before running any phase or scrape command, collect and confirm:

1. Company name
2. Website URL

Do not scrape or create files until both values are confirmed.

## Mandatory Phase-End Review Gate (Phases 1-11)

After each phase output, always pause and ask the user to choose one option:

- `Continue to next phase`
- `Update this phase now`
- `Stop for now`

If user chooses `Update this phase now`, update phase outputs and re-run the same gate.
Do not auto-advance to the next phase unless user explicitly chooses `Continue to next phase`.

Use this canonical prompt:

`Review complete phase output? Choose: [Continue to next phase] [Update this phase now] [Stop for now]`

## 🔍 SCRAPING WITH PYTHON SCRIPT

**Use the Python script for all web scraping:**

```bash
# Scrape a URL (log to company directory)
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d brains/{company-slug}/

# Scrape homepage + 1 level of subpages (saves to brains/{company-slug}/scraped/ for later use)
python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com -d brains/{company-slug}/ --subpages

# Scrape and save to JSON file
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d brains/{company-slug}/ -o output.json
```

The script extracts: title, description, headings, links, and text content.
The `-d` flag specifies where to write `scraping.log`.

**Strategy**: Scrape first, validate with user second.

## V1 Output Requirements (Mandatory)

For every object created in this workflow, enforce `templates/V1-CONTRACT.md`:

- Include YAML frontmatter (`object_type`, `company`, `version`, `last_updated`, `last_verified`, `confidence`, `source_urls`, `tags`).
- Include required sections: `Overview`, `Evidence & Sources`, `Operator Guidance`, `Cross-References`.
- If proof is missing, write `To be verified` instead of inventing metrics.

## Use existing scraped data first

Before scraping in a phase, **check** `brains/{company-slug}/scraped/`:

```bash
python .cursor/rules/sales-brain/scripts/scrape.py load-scraped -d brains/{company-slug}/
python .cursor/rules/sales-brain/scripts/scrape.py load-scraped -d brains/{company-slug}/ -p products
```

If `scraped/index.json` and `main.json` exist, **use that data** for the phase (e.g. main.json for company; product/solutions subpages for products and personas). Only run new scrapes for URLs not already in scraped/, or when scraped/ is empty.

## Company Directory Structure

**IMPORTANT**: All files for a company are stored in a company-specific directory.

When starting:
1. Ask for company name and website URL
2. Create company directory: `brains/{company-slug}/` (lowercase, hyphens)
3. All files go inside this directory

```
brains/{company-slug}/
├── company.md
├── scraped/           # main.json, index.json, subpage .json (use in phases before scraping)
├── products/
├── target-companies.md
├── personas/
├── pain-points/
├── value-propositions/
├── use-cases/
├── competitors/
├── objections/
├── case-studies/
├── sales-plays/
└── scraping.log (URLs scraped)
```

## Full Workflow (11 Phases)

### Phase 1: Company Research
1. **Ask for**: Company name + Website URL (strictly before any scraping)
2. **Create directory**: `brains/{company-slug}/`
3. **🔍 SCRAPE** using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/about -d brains/{company-slug}/
   ```
4. **Create** `brains/{company-slug}/company.md`
5. **Present findings** and ask for confirmation
6. **Run mandatory phase-end review gate** (continue/update/stop)

### Phase 2: Product Detection
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/products -d brains/{company-slug}/`
- Create `brains/{company-slug}/products/{product-slug}.md` files
- Run mandatory phase-end review gate (continue/update/stop)

### Phase 3: Target Companies
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/customers -d brains/{company-slug}/`
- Ask user for additional context
- Create `brains/{company-slug}/target-companies.md`
- Run mandatory phase-end review gate (continue/update/stop)

### Phase 4: Personas
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/solutions -d brains/{company-slug}/`
- Ask user to identify personas
- Create `brains/{company-slug}/personas/{persona-slug}.md` files
- Run mandatory phase-end review gate (continue/update/stop)

### Phase 5: Pain Points
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/products/company/reviews -d brains/{company-slug}/`
- Create `brains/{company-slug}/pain-points/{persona}-pain-points.md` files
- Run mandatory phase-end review gate (continue/update/stop)

### Phase 6: Value Propositions
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/roi -d brains/{company-slug}/`
- Create `brains/{company-slug}/value-propositions/{product}-{persona}.md` files
- Run mandatory phase-end review gate (continue/update/stop)

### Phase 7: Use Cases
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/case-studies -d brains/{company-slug}/`
- Create `brains/{company-slug}/use-cases/{use-case}.md` files
- Run mandatory phase-end review gate (continue/update/stop)

### Phase 8: Competitive Intelligence
- **🔍 SCRAPE COMPETITOR WEBSITES**:
  ```bash
  python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com -d brains/{company-slug}/
  python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com/products -d brains/{company-slug}/
  ```
- Create `brains/{company-slug}/competitors/{competitor}.md` files
- Run mandatory phase-end review gate (continue/update/stop)

### Phase 9: Objection Handling
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/products/company/reviews -d brains/{company-slug}/`
- Create `brains/{company-slug}/objections/{persona}-objections.md` files
- Run mandatory phase-end review gate (continue/update/stop)

### Phase 10: Case Studies
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/customers/story -d brains/{company-slug}/`
- Create `brains/{company-slug}/case-studies/{customer}.md` files
- Run mandatory phase-end review gate (continue/update/stop)

### Phase 11: Sales Plays
- **Synthesize** all gathered information
- Create `brains/{company-slug}/sales-plays/{play}.md` files
- Run mandatory phase-end review gate (continue/update/stop)

### Final Step: Generate INDEX.md and README.md
- **Auto-generate** `brains/{company-slug}/INDEX.md` - File inventory, loading rules
- **Auto-generate** `brains/{company-slug}/README.md` - Human-friendly overview (GitHub/file browser default)
- README helps humans; INDEX helps AI agents load context efficiently
- Run mandatory phase-end review gate for final output

## Scraping Checklist by Phase

| Phase | Python Scrape Commands |
|-------|----------------------|
| 1. Company | Homepage, About pages |
| 2. Products | Product, Platform, Pricing pages |
| 3. Target Companies | Customers, Case studies list |
| 4. Personas | Solutions by role pages |
| 5. Pain Points | G2 reviews, Challenge pages |
| 6. Value Props | ROI, Testimonial pages |
| 7. Use Cases | Case studies, Solutions pages |
| 8. Competitors | **Competitor websites directly** |
| 9. Objections | G2 reviews, FAQ pages |
| 10. Case Studies | Customer stories pages |
| 11. Sales Plays | Synthesis (no scraping) |

## Important Guidelines
- **Create company directory first** before any files
- **Use Python script** for all scraping: `python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d brains/{company-slug}/`
- **Always use `-d` flag** to log scrapes to the company directory
- **Scrape before asking** - research first, validate second
- Use URL-friendly slug for company name (lowercase, hyphens)
- All files go inside the company directory (`brains/{company-slug}/`)
- Reference templates from `templates/` directory
- User can skip phases or use individual `/add` commands
