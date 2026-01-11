---
description: "Sales Brain 11-phase workflow with Python scraping. Use when running /start command or executing any phase of the sales research workflow."
alwaysApply: true
---

# Sales Brain Workflow (11 Phases)

## Web Scraping with Python Script

**USE THE PYTHON SCRIPT** for all web scraping throughout the workflow:

```bash
# Scrape a URL and output JSON
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url>

# Scrape and save to file
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -o output.json
```

The script extracts:
- Page title and meta description
- All headings (h1, h2, h3)
- Important links (about, products, pricing, contact)
- Main text content

**Strategy**: Scrape first, validate with user second.

## Phase 1: Company Research (Foundation)

1. Ask the user for:
   - Company name
   - Website URL

2. **Create company directory**:
   - Convert company name to URL-friendly slug (lowercase, hyphens)
   - Create directory: `{company-slug}/`
   - All subsequent files go inside this directory

3. **🔍 SCRAPE** the company website using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/about
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/products
   ```

4. Create `{company-slug}/company.md` with structured company information

5. Present findings and ask user to confirm accuracy
   - If confirmed → proceed to Phase 2
   - If not confirmed → ask what to change, update file, re-confirm

## Phase 2: Product Detection

1. **🔍 SCRAPE** product pages using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/products
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/platform
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/pricing
   ```

2. Create `{company-slug}/products/` directory if it doesn't exist
3. For each product, create `{company-slug}/products/{product-slug}.md`
4. Present product summaries to user

## Phase 3: Target Companies Research

1. **🔍 SCRAPE** for target company info using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/customers
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/case-studies
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/industries
   ```

2. Ask the user about target companies:
   - What types of companies do you sell to?
   - Industry, size, characteristics
   - Why they buy your products
   - Common challenges they face

3. Create `{company-slug}/target-companies.md` with structured information

## Phase 4: Persona Research

1. **🔍 SCRAPE** for persona info using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/solutions
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/for-sales-teams
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/for-marketing
   ```

2. Ask the user to identify target personas (generic roles, not company-specific)
3. For each persona, gather:
   - Persona name/title
   - Role and responsibilities
   - Company size/type they typically work for
   - Key problems and pain points
   - Goals and objectives
   - How the company's products solve their problems

4. Create `{company-slug}/personas/` directory if it doesn't exist
5. For each persona, create `{company-slug}/personas/{persona-slug}.md`
6. Present persona summaries to user

## Phase 5: Pain Points Deep Dive

1. **🔍 SCRAPE** for pain points using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/products/company/reviews
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/challenges
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/why-us
   ```

2. For each persona, document detailed pain points:
   - Specific problems and their impact
   - Current solutions they use
   - Frequency and severity
   - Which products address each pain point

3. Create `{company-slug}/pain-points/` directory if it doesn't exist
4. For each persona, create `{company-slug}/pain-points/{persona-slug}-pain-points.md`

## Phase 6: Value Propositions

1. **🔍 SCRAPE** for messaging using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/roi
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/testimonials
   ```

2. Map products to personas with specific value propositions:
   - The problem solved
   - Key value drivers
   - Quantified benefits
   - ROI story
   - Messaging framework

3. Create `{company-slug}/value-propositions/` directory if it doesn't exist
4. Create `{company-slug}/value-propositions/{product-slug}-{persona-slug}.md` files

## Phase 7: Use Cases

1. **🔍 SCRAPE** for use cases using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/case-studies
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/solutions
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/use-cases
   ```

2. For each use case, document:
   - Context and trigger events
   - The challenge and solution
   - Products involved
   - Value delivered
   - Proof points

3. Create `{company-slug}/use-cases/` directory if it doesn't exist
4. Create `{company-slug}/use-cases/{use-case-slug}.md` files

## Phase 8: Competitive Intelligence

1. **🔍 SCRAPE COMPETITOR WEBSITES DIRECTLY** using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com/products
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com/pricing
   ```

2. Also scrape comparison pages:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/vs-competitor
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/compare/company-vs-competitor
   ```

3. For each competitor, document:
   - Company overview
   - Product comparison
   - Strengths and weaknesses
   - Competitive battlecard
   - How to win against them

4. Create `{company-slug}/competitors/` directory if it doesn't exist
5. Create `{company-slug}/competitors/{competitor-slug}.md` files

## Phase 9: Objection Handling

1. **🔍 SCRAPE** for objections using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/products/company/reviews
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/faq
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com/why-switch
   ```

2. For each persona, document common objections:
   - Why they say it
   - How to acknowledge
   - How to respond
   - Proof points

3. Create `{company-slug}/objections/` directory if it doesn't exist
4. Create `{company-slug}/objections/{persona-slug}-objections.md` files

## Phase 10: Case Studies

1. **🔍 SCRAPE** customer stories using Python:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/customers
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/case-studies/customer-name
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/press
   ```

2. For each case study, include:
   - Customer overview
   - Challenge they faced
   - Solution implemented
   - Results achieved
   - Quotes

3. Create `{company-slug}/case-studies/` directory if it doesn't exist
4. Create `{company-slug}/case-studies/{customer-slug}.md` files

## Phase 11: Sales Plays

1. **Synthesize** all scraped and gathered information
2. Create actionable sales playbooks:
   - When to run the play
   - Target persona and company
   - Execution steps
   - Messaging and scripts
   - Success metrics

3. Create `{company-slug}/sales-plays/` directory if it doesn't exist
4. Create `{company-slug}/sales-plays/{play-slug}.md` files

## Final Step: Generate INDEX.md and SUMMARY.md

After completing all 11 phases, **automatically generate context files**:

### Generate INDEX.md
1. Scan all files created in `{company-slug}/`
2. Generate `{company-slug}/INDEX.md` with:
   - Quick reference (company, products, personas)
   - File inventory by category
   - Loading rules for AI agents
   - Topic → file mapping

### Generate SUMMARY.md
1. Extract key info from all files
2. Generate `{company-slug}/SUMMARY.md` (~1000 tokens) with:
   - Company overview (1 paragraph)
   - Products table (1-line each)
   - Personas with key pain + value
   - Top competitors
   - Common objections with quick responses
   - Proof points from case studies
   - Sales play triggers

3. Show completion summary

These files help AI agents know what context is available and load efficiently.

## Scraping Best Practices

1. **Scrape first, ask second** - Research before asking user for input
2. **Multiple pages** - Don't just scrape homepage, go deep into site
3. **Competitor sites** - Directly scrape competitor websites for accurate info
4. **Review sites** - G2, Gartner for real customer feedback
5. **Save time** - Scraping provides 80% of info, user validates 20%
6. **Handle failures** - If scraping fails, fall back to asking user
7. **Check scraping.txt** - Track pages scraped count in company directory
