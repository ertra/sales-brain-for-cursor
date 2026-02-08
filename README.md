# 🧠 Sales Brain for Cursor

An AI-powered sales research assistant for gathering and organizing company and product intelligence.

## What is Sales Brain?

Sales Brain is a **Cursor-based workflow** that helps you build a comprehensive sales intelligence package for your company. It uses AI to research, organize, and structure everything your sales team needs to sell effectively.

### What it creates

- **Company profile** - Your company's overview, mission, differentiators, target market
- **Product documentation** - Features, value props, competitive positioning for each product
- **Buyer personas** - Target roles, their pain points, goals, discovery questions
- **Competitive battlecards** - Head-to-head comparisons with competitors, when you win/lose
- **Objection handling** - Common objections with proven responses
- **Sales plays** - Actionable playbooks for specific selling situations
- **Case studies** - Customer success stories with metrics

### Who it's for

- **Founders** building go-to-market materials from scratch
- **Sales leaders** creating enablement content for their team
- **Sales enablement** standardizing messaging and playbooks
- **RevOps** documenting sales processes and competitive intel

### How it works

1. Type `/start` in Cursor
2. Provide your company name and website
3. AI scrapes your public information and generates structured sales intelligence
4. Review, refine, and add your proprietary insights
5. Your sales team uses the output for prospecting, pitching, and closing

---

## Quick Start

### Setup

1. Run the setup script:
```bash
./setup.sh
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

3. Open the project in **Cursor**

### Usage

**In Cursor:**
```
/start
```

Then follow the 11-phase workflow:
1. Company research
2. Product detection
3. Target companies
4. Personas
5. Pain points
6. Value propositions
7. Use cases
8. Competitive intelligence
9. Objection handling
10. Case studies
11. Sales plays  
12. **Final step:** Auto-generate `INDEX.md` (file inventory & loading rules) and `README.md` (folder overview) for the company

All generated content follows the **templates** in `templates/` (see [Templates](#templates) below).

## Templates

All generated content follows **templates** in `templates/`. Use them for consistency when adding or editing objects.

| Template | Used for |
|----------|----------|
| `company-template.md` | Company overview, mission, differentiators, scraped info |
| `target-companies-template.md` | ICP, company profiles by type, qualification |
| `product-template.md` | Product overview, features, value prop, competition |
| `persona-template.md` | Role, responsibilities, pain points, goals, buying process |
| `pain-points-template.md` | Pain points (description, impact, solution, key message), priority matrix, discovery questions, trigger events |
| `value-proposition-template.md` | Summary, problem/solution, value drivers, quantified value, ROI story, messaging framework, competitive positioning |
| `use-case-template.md` | Context, challenge (before/after), solution, value delivered, proof points, sales conversation guide |
| `competitor-template.md` | Overview, products, strengths/weaknesses, feature comparison, battlecard, objection handling |
| `objection-template.md` | Objections with acknowledge, respond, proof point, follow-up question; prevention; quick reference |
| `case-study-template.md` | Snapshot, executive summary, customer/challenge/solution/results, quotes, sales use, related objects |
| `sales-play-template.md` | Play overview, trigger events, qualification, execution steps, objection handling, resources |

## Output Structure

Each company gets its own directory under `brains/` with all sales intelligence files. After the full workflow, **INDEX.md** and **README.md** are auto-generated for that company.

```
sales-brain-for-cursor/
├── templates/              # Templates for all objects (shared)
├── brains/                 # All company research lives here
│   ├── {company-slug}/     # Company-specific directory
│   │   ├── INDEX.md        # Auto-generated: file inventory & loading rules for AI
│   │   ├── README.md       # Auto-generated: human-friendly folder overview (GitHub default)
│   │   ├── company.md      # Company overview
│   │   ├── scraped/        # Scraped JSON (main.json, products, case-studies, etc.); use before re-scraping
│   │   ├── products/
│   │   ├── target-companies.md
│   │   ├── personas/
│   │   ├── pain-points/
│   │   ├── value-propositions/
│   │   ├── use-cases/
│   │   ├── competitors/
│   │   ├── objections/
│   │   ├── case-studies/
│   │   ├── sales-plays/
│   │   └── scraping.log    # URLs scraped (written when using -d)
│   └── {another-company}/
└── ...
```

## Example Companies

Full Sales Brain examples (all 11 phases + INDEX/README) are in `brains/apollo/` and `brains/revenue-io/`. Other examples: `brains/salesloft/`, `brains/gong/`, `brains/lautie/`.

**Example: Revenue.io** (recent full run):

```
brains/revenue-io/
├── INDEX.md                    # File inventory & loading rules for AI
├── README.md                   # Folder overview, proof points, quick links
├── company.md
├── target-companies.md
├── scraped/                    # main.json, products.json, case-study-*.json, competitor-*.json, etc.
├── products/                   # 11 products (revenue-platform, salesforce-dialer, moments, ...)
├── personas/                   # 8 personas (sales-leader, account-executive, revops, ...)
├── pain-points/               # 8 persona pain-point files
├── value-propositions/        # 6 product–persona value props
├── use-cases/                 # 5 use cases
├── competitors/               # Gong, Outreach, Salesloft
├── objections/                # common + sales-leader, revenue-operations, account-executive
├── case-studies/              # HPE, Nutanix, OrthoFX, FreshBooks, NFI Industries
└── sales-plays/               # Consolidation, Real-time coaching, Scale meetings
```

## Commands

**Note:** Most commands require `{company}` parameter (e.g., `salesloft`).

| Command | Description |
|---------|-------------|
| `/start` | Begin the full 11-phase workflow |
| `/continue {company}` | Continue workflow (e.g., `/continue salesloft`) |
| `/status` | List all companies with summary |
| `/status {company}` | Detailed status with freshness indicators |
| `/search {company} {query}` | Search all files (e.g., `/search salesloft ROI`) |
| `/refresh {company}` | Full refresh - re-scrapes all sources |
| `/generate-index {company}` | Generate INDEX.md (file inventory) |
| `/generate-readme {company}` | Generate README.md (folder overview) |
| `/generate-visualization {company}` | Generate interactive HTML graph |
| `/list all` | List all companies |
| `/list all {company}` | List all objects for a company |
| `/list products {company}` | List products |
| `/list personas {company}` | List personas |
| `/add product {company}` | Add a new product |
| `/add persona {company}` | Add a new persona |
| `/add pain-points {company}` | Add pain points for a persona |
| `/add value-prop {company}` | Add value proposition |
| `/add use-case {company}` | Add a use case scenario |
| `/add competitor {company}` | Add competitive intelligence |
| `/add objections {company}` | Add objection handling |
| `/add case-study {company}` | Add a customer success story |
| `/add sales-play {company}` | Add a sales playbook |
| `/update company {company}` | Re-research company info |
| `/update target-companies {company}` | Update target companies |

## File Formats

Generated files follow the **templates** in `templates/`. Summary by type:

### README.md & INDEX.md (company folder)
- **README.md** — Auto-generated; company tagline, proof points table, differentiators, folder structure, quick links. Shown by default on GitHub.
- **INDEX.md** — Auto-generated; file inventory by category, loading rules for AI agents, topic → file mapping. Use for context loading.

**Use README.md for a one-page overview; use INDEX.md for full file list and when to load which file.**

### company.md
Company overview, industry, founded, headquarters, size, mission/vision, target market, key differentiators, website, scraped information (headings, links), additional notes.

### target-companies.md
Overview of target segments; company profiles (industry, size, characteristics, why they buy, common challenges); referenced customers; additional notes.

### products/{product-name}.md
Company, overview, main features, problem solved, value proposition, target customers, competition table, pricing model, additional notes.

### personas/{persona-name}.md
Role/title, responsibilities, company profile, key problems & pain points, goals & objectives, how our products solve their problems, buying process, communication preferences, additional notes.

### pain-points/{persona}-pain-points.md
Overview; pain points (description, impact, current solutions, frequency, severity, product solution, key message); pain point priority matrix; discovery questions; trigger events; quick reference table.

### value-propositions/{product}-{persona}.md
Summary, problem, solution; key value drivers (benefit, proof point, customer quote); quantified value table; ROI story; messaging framework (elevator pitch, email subject lines, key phrases, avoid); competitive positioning.

### use-cases/{use-case}.md
Overview; context (target company profile, primary persona, trigger event); challenge (current/desired state); solution (products, steps); value delivered (quantified + qualitative); proof points (customer examples, data); sales conversation guide (discovery questions, demo focus, talking points); related objects.

### competitors/{competitor}.md
Overview, company info, product overview, positioning & messaging, strengths/weaknesses, feature comparison, competitive battlecard (when we win/lose, differentiators, their claims vs reality), handling competitive situations, trap-setting questions, pricing comparison, resources.

### objections/{persona}-objections.md or common-objections.md
Objections with: why they say this, acknowledge, respond, proof point, follow-up question; objection prevention (questions to ask early, red flags); quick reference table.

### case-studies/{customer}.md
Snapshot table; executive summary; the customer; challenge (situation, pain points, impact, what they tried); solution (why they chose us, products, timeline); results (metrics table, headline results, qualitative benefits); customer quotes; sales use (best for, talking points, objections this addresses); related objects; resources.

### sales-plays/{play}.md
Play overview table; when to run (trigger events, ideal signals, qualification criteria); objective & value proposition; execution steps (research, outreach, discovery, demo, proposal); objection handling table; resources & tools; success metrics; related objects.

## Configuration

- **`.cursor/rules/`** — Cursor AI rules (workflow, sales-brain scraping, templates)
- **`.cursor/commands/`** — Slash commands (e.g. `start.md`, `continue.md`, `add-*.md`, `generate-index.md`)
- **`templates/`** — Markdown templates for every object type (company, product, persona, pain-points, value-proposition, use-case, competitor, objection, case-study, sales-play)

## Tips

1. **Be specific** when entering the company name
2. **Use the main website URL** (not subpages)
3. **Review carefully** before confirming - the AI will research based on your approval
4. **Add products manually** if automatic detection misses some
5. **Check scraping.log** to see which URLs were scraped
6. **Load README.md or INDEX.md** when using AI agents for company context

## Web Scraping

Sales Brain uses a **Python script** for all web scraping (`.cursor/rules/sales-brain/scripts/scrape.py`). The workflow uses `-d brains/{company-slug}/` so every scrape is logged to that company’s `scraping.log`.

```bash
# Scrape a URL (log to company directory)
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d brains/{company-slug}/

# Scrape homepage + 1 level of subpages (saves to scraped/ for later use)
python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com -d brains/{company-slug}/ --subpages

# Scrape and save to JSON (e.g. for use in phases)
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d brains/{company-slug}/ -o brains/{company-slug}/scraped/main.json

# Load existing scraped data (check before re-scraping)
python .cursor/rules/sales-brain/scripts/scrape.py load-scraped -d brains/{company-slug}/
python .cursor/rules/sales-brain/scripts/scrape.py load-scraped -d brains/{company-slug}/ -p products
```

**Options:**
- `-d, --log-dir` — Directory for `scraping.log` (and where to find/save scraped data)
- `-o, --output` — Save JSON output to file (e.g. `brains/{company-slug}/scraped/products.json`)
- `--subpages` — Scrape homepage + one level of subpages; saves to company `scraped/` for use in phases
- `-f, --follow` — Follow discovered links (about, products, pricing, contact, all)
- `-m, --max-pages` — Maximum pages when following links (default: 10)

**Extracted data:** Page title, meta description, headings (h1–h3), important links (about, products, pricing, contact), main text content.

**Strategy:** Use existing files in `brains/{company-slug}/scraped/` when present (e.g. `main.json`, product or case-study JSON). Only run new scrapes for URLs not already covered or when `scraped/` is empty. Scrape first, validate with user second.

## ⚠️ Disclaimer

**The example company data in this repository (e.g. `brains/apollo/`, `brains/revenue-io/`, `brains/salesloft/`, `brains/gong/`, `brains/lautie/`) is for demonstration purposes only.**

- All information was gathered from **publicly available sources** (company websites, public documentation, case study pages)
- This data illustrates how the tool works and what output to expect
- Example playbooks, battlecards, objection handling, and case studies are **samples** to demonstrate the framework
- **This is not official sales material** from any company mentioned
- For real sales use, generate your own research and add proprietary insights

The **framework, templates, and tooling** are the primary value of this project.

## Authors

**Tomas Zeman**  
📧 tomas.zeman@gmail.com

## License

MIT
