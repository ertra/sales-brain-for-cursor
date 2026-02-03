---
description: "Sales Brain 11-phase workflow with Python scraping. Use when running /start command or executing any phase of the sales research workflow."
alwaysApply: true
---

# Sales Brain Workflow (11 Phases)

## Web Scraping with Python Script

**USE THE PYTHON SCRIPT** for all web scraping throughout the workflow:

```bash
# Scrape a URL and output JSON (use -d so scraping.log goes to company dir)
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d brains/{company-slug}/

# Scrape and save to file
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d brains/{company-slug}/ -o output.json
```

The script extracts:
- Page title and meta description
- All headings (h1, h2, h3)
- Important links (about, products, pricing, contact)
- Main text content

**Strategy**: Scrape first, validate with user second.

## Use existing scraped data first

Before scraping in any phase, **check if useful data already exists** in `brains/{company-slug}/scraped/`:

```bash
# See what's in scraped/ (main_url, subpage count, slugs)
python .cursor/rules/sales-brain/scripts/scrape.py load-scraped -d brains/{company-slug}/

# See pages relevant to a phase (products, personas, case-studies, etc.)
python .cursor/rules/sales-brain/scripts/scrape.py load-scraped -d brains/{company-slug}/ -p products
```

- If `scraped/index.json` and `scraped/main.json` exist, **use that data** for the current phase:
  - **Phase 1 (Company)**: Use `scraped/main.json` (and optionally other subpages) to create or update `company.md`.
  - **Phase 2 (Products)**: Use subpage JSONs whose slug/URL suggest products (e.g. `platform`, `platform-*`, `solutions`, `pricing`, `collective`). Only scrape extra URLs if needed.
  - **Phase 3 (Target companies)**: Use pages like `case-studies`, `customers`, `industries` from scraped/.
  - **Phase 4 (Personas)**: Use `solutions*`, role-related subpages from scraped/.
  - **Phase 5–7, 9–10**: Similarly use scraped subpages that match the phase topic (reviews, challenges, case-studies, etc.).
- **Scrape only when**: scraped/ is missing, or the phase needs URLs not yet in scraped/ (e.g. a specific competitor, G2 reviews). Same as now, steps can still run their own scrape for a single URL or use `--subpages` to (re)fill scraped/.

## Phase 1: Company Research (Foundation)

1. Ask the user for:
   - Company name
   - Website URL

2. **Create company directory**:
   - Convert company name to URL-friendly slug (lowercase, hyphens)
   - Create directory: `brains/{company-slug}/`
   - All subsequent files go inside this directory

3. **🔍 SCRAPE** the company website using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/about -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/products -d brains/{company-slug}/
   ```

4. Create `brains/{company-slug}/company.md` with structured company information

5. Present findings and ask user to confirm accuracy
   - If confirmed → proceed to Phase 2
   - If not confirmed → ask what to change, update file, re-confirm

## Phase 2: Product Detection

1. **🔍 SCRAPE** product pages using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/products -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/platform -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/pricing -d brains/{company-slug}/
   ```

2. Create `brains/{company-slug}/products/` directory if it doesn't exist
3. For each product, create `brains/{company-slug}/products/{product-slug}.md`
4. Present product summaries to user

## Phase 3: Target Companies Research

1. **🔍 SCRAPE** for target company info using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/customers -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/case-studies -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/industries -d brains/{company-slug}/
   ```

2. Ask the user about target companies:
   - What types of companies do you sell to?
   - Industry, size, characteristics
   - Why they buy your products
   - Common challenges they face

3. Create `brains/{company-slug}/target-companies.md` with structured information

## Phase 4: Persona Research

1. **🔍 SCRAPE** for persona info using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/solutions -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/for-sales-teams -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/for-marketing -d brains/{company-slug}/
   ```

2. Ask the user to identify target personas (generic roles, not company-specific)
3. For each persona, gather:
   - Persona name/title
   - Role and responsibilities
   - Company size/type they typically work for
   - Key problems and pain points
   - Goals and objectives
   - How the company's products solve their problems

4. Create `brains/{company-slug}/personas/` directory if it doesn't exist
5. For each persona, create `brains/{company-slug}/personas/{persona-slug}.md`
6. Present persona summaries to user

## Phase 5: Pain Points Deep Dive

1. **🔍 SCRAPE** for pain points using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/products/company/reviews -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/challenges -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/why-us -d brains/{company-slug}/
   ```

2. For each persona, document detailed pain points:
   - Specific problems and their impact
   - Current solutions they use
   - Frequency and severity
   - Which products address each pain point

3. Create `brains/{company-slug}/pain-points/` directory if it doesn't exist
4. For each persona, create `brains/{company-slug}/pain-points/{persona-slug}-pain-points.md`

## Phase 6: Value Propositions

1. **🔍 SCRAPE** for messaging using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/roi -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/testimonials -d brains/{company-slug}/
   ```

2. Map products to personas with specific value propositions:
   - The problem solved
   - Key value drivers
   - Quantified benefits
   - ROI story
   - Messaging framework

3. Create `brains/{company-slug}/value-propositions/` directory if it doesn't exist
4. Create `brains/{company-slug}/value-propositions/{product-slug}-{persona-slug}.md` files

## Phase 7: Use Cases

1. **🔍 SCRAPE** for use cases using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/case-studies -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/solutions -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/use-cases -d brains/{company-slug}/
   ```

2. For each use case, document:
   - Context and trigger events
   - The challenge and solution
   - Products involved
   - Value delivered
   - Proof points

3. Create `brains/{company-slug}/use-cases/` directory if it doesn't exist
4. Create `brains/{company-slug}/use-cases/{use-case-slug}.md` files

## Phase 8: Competitive Intelligence

1. **🔍 SCRAPE COMPETITOR WEBSITES DIRECTLY** using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com/products -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com/pricing -d brains/{company-slug}/
   ```

2. Also scrape comparison pages:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/vs-competitor -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/compare/company-vs-competitor -d brains/{company-slug}/
   ```

3. For each competitor, document:
   - Company overview
   - Product comparison
   - Strengths and weaknesses
   - Competitive battlecard
   - How to win against them

4. Create `brains/{company-slug}/competitors/` directory if it doesn't exist
5. Create `brains/{company-slug}/competitors/{competitor-slug}.md` files

## Phase 9: Objection Handling

1. **🔍 SCRAPE** for objections using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/products/company/reviews -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/faq -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com/why-switch -d brains/{company-slug}/
   ```

2. For each persona, document common objections:
   - Why they say it
   - How to acknowledge
   - How to respond
   - Proof points

3. Create `brains/{company-slug}/objections/` directory if it doesn't exist
4. Create `brains/{company-slug}/objections/{persona-slug}-objections.md` files

## Phase 10: Case Studies

1. **🔍 SCRAPE** customer stories using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/customers -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/case-studies/customer-name -d brains/{company-slug}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/press -d brains/{company-slug}/
   ```

2. For each case study, include:
   - Customer overview
   - Challenge they faced
   - Solution implemented
   - Results achieved
   - Quotes

3. Create `brains/{company-slug}/case-studies/` directory if it doesn't exist
4. Create `brains/{company-slug}/case-studies/{customer-slug}.md` files

## Phase 11: Sales Plays

1. **Synthesize** all scraped and gathered information
2. Create actionable sales playbooks:
   - When to run the play
   - Target persona and company
   - Execution steps
   - Messaging and scripts
   - Success metrics

3. Create `brains/{company-slug}/sales-plays/` directory if it doesn't exist
4. Create `brains/{company-slug}/sales-plays/{play-slug}.md` files

## Final Step: Generate INDEX.md and README.md

After completing all 11 phases, **automatically generate context files**:

### Generate INDEX.md
1. Scan all files created in `brains/{company-slug}/`
2. Generate `brains/{company-slug}/INDEX.md` with:
   - Quick reference (company, products, personas)
   - File inventory by category
   - Loading rules for AI agents
   - Topic → file mapping

### Generate README.md
1. Gather content from `company.md` and existing sections
2. Generate `brains/{company-slug}/README.md` (human-friendly overview) with:
   - Company name and tagline
   - Short summary (2–4 sentences) and link to website
   - "What's in this folder" table (company.md, INDEX.md, products/, personas/, etc.)
   - Quick start (how to use the folder)
   - Omit rows for sections that don't exist

3. Show completion summary

README.md is shown by default on GitHub and in file browsers; INDEX.md helps AI agents load context efficiently.

## Scraping Best Practices

1. **Scrape first, ask second** - Research before asking user for input
2. **Multiple pages** - Don't just scrape homepage, go deep into site
3. **Competitor sites** - Directly scrape competitor websites for accurate info
4. **Review sites** - G2, Gartner for real customer feedback
5. **Save time** - Scraping provides 80% of info, user validates 20%
6. **Handle failures** - If scraping fails, fall back to asking user
7. **Check scraping.txt** - Track pages scraped count in company directory
