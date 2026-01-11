# Start Sales Brain Workflow

When the user types `/start`, begin the Sales Brain research workflow.

## 🔍 SCRAPING WITH PYTHON SCRIPT

**Use the Python script for all web scraping:**

```bash
# Scrape a URL (log to company directory)
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d {company-slug}/

# Scrape and save to JSON file
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d {company-slug}/ -o output.json
```

The script extracts: title, description, headings, links, and text content.
The `-d` flag specifies where to write `scraping.log`.

**Strategy**: Scrape first, validate with user second.

## Company Directory Structure

**IMPORTANT**: All files for a company are stored in a company-specific directory.

When starting:
1. Ask for company name and website URL
2. Create company directory: `{company-slug}/` (lowercase, hyphens)
3. All files go inside this directory

```
{company-slug}/
├── company.md
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
1. **Ask for**: Company name + Website URL
2. **Create directory**: `{company-slug}/`
3. **🔍 SCRAPE** using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com -d {company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/about -d {company-slug}/
   ```
4. **Create** `{company-slug}/company.md`
5. **Present findings** and ask for confirmation

### Phase 2: Product Detection
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/products -d {company-slug}/`
- Create `{company-slug}/products/{product-slug}.md` files

### Phase 3: Target Companies
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/customers -d {company-slug}/`
- Ask user for additional context
- Create `{company-slug}/target-companies.md`

### Phase 4: Personas
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/solutions -d {company-slug}/`
- Ask user to identify personas
- Create `{company-slug}/personas/{persona-slug}.md` files

### Phase 5: Pain Points
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/products/company/reviews -d {company-slug}/`
- Create `{company-slug}/pain-points/{persona}-pain-points.md` files

### Phase 6: Value Propositions
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/roi -d {company-slug}/`
- Create `{company-slug}/value-propositions/{product}-{persona}.md` files

### Phase 7: Use Cases
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/case-studies -d {company-slug}/`
- Create `{company-slug}/use-cases/{use-case}.md` files

### Phase 8: Competitive Intelligence
- **🔍 SCRAPE COMPETITOR WEBSITES**:
  ```bash
  python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com -d {company-slug}/
  python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com/products -d {company-slug}/
  ```
- Create `{company-slug}/competitors/{competitor}.md` files

### Phase 9: Objection Handling
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/products/company/reviews -d {company-slug}/`
- Create `{company-slug}/objections/{persona}-objections.md` files

### Phase 10: Case Studies
- **🔍 SCRAPE**: `python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/customers/story -d {company-slug}/`
- Create `{company-slug}/case-studies/{customer}.md` files

### Phase 11: Sales Plays
- **Synthesize** all gathered information
- Create `{company-slug}/sales-plays/{play}.md` files

### Final Step: Generate INDEX.md and SUMMARY.md
- **Auto-generate** `{company-slug}/INDEX.md` - File inventory, loading rules
- **Auto-generate** `{company-slug}/SUMMARY.md` - Condensed context (~1000 tokens)
- These help AI agents load context efficiently

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
- **Use Python script** for all scraping: `python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d {company-slug}/`
- **Always use `-d` flag** to log scrapes to the company directory
- **Scrape before asking** - research first, validate second
- Use URL-friendly slug for company name (lowercase, hyphens)
- All files go inside the company directory
- Reference templates from `templates/` directory
- User can skip phases or use individual `/add` commands
