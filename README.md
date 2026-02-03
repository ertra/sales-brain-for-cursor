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

## Output Structure

Each company gets its own directory under `brains/` with all sales intelligence files:

```
sales-brain-for-cursor/
├── templates/              # Templates for all objects (shared)
├── brains/                 # All company research lives here
│   ├── {company-slug}/     # Company-specific directory
│   │   ├── INDEX.md        # Auto-generated file inventory
│   │   ├── README.md       # Auto-generated folder overview (GitHub default)
│   │   ├── company.md      # Company overview
│   │   ├── products/       # Products
│   │   ├── target-companies.md
│   │   ├── personas/       # Buyer personas
│   │   ├── pain-points/    # Pain points by persona
│   │   ├── value-propositions/
│   │   ├── use-cases/
│   │   ├── competitors/
│   │   ├── objections/
│   │   ├── case-studies/
│   │   ├── sales-plays/
│   │   └── scraping.log    # URLs scraped log
│   └── {another-company}/  # Another company...
└── ...
```

## Example: Salesloft

A complete example is included in `brains/salesloft/`:

```
brains/salesloft/
├── INDEX.md                    # File inventory & loading rules
├── README.md                   # Folder overview (GitHub default)
├── company.md                  # Company overview
├── target-companies.md         # ICP & buying committee
├── products/                   # 8 products documented
│   ├── cadence.md
│   ├── rhythm.md
│   ├── conversations.md
│   ├── drift.md
│   ├── deals.md
│   ├── forecast.md
│   ├── analytics.md
│   └── ai-agents.md
├── personas/                   # 6 personas profiled
│   ├── cro.md
│   ├── sales-leader.md
│   ├── sales-manager.md
│   ├── revenue-operations.md
│   ├── account-executive.md
│   └── sdr-bdr.md
├── pain-points/
├── value-propositions/
├── use-cases/
├── competitors/                # 2 battlecards
│   ├── outreach.md
│   └── gong.md
├── objections/
├── case-studies/
└── sales-plays/                # 2 sales plays
    ├── competitive-displacement.md
    └── new-sales-leader.md
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

### README.md
Auto-generated folder overview (shown by default on GitHub):
- Company name and tagline
- Short summary and website link
- "What's in this folder" table
- Quick start for using the Sales Brain

**Open README.md for a one-page overview; use INDEX.md for full file list and loading rules.**

### company.md
Contains:
- Company overview
- Industry & headquarters
- Mission/vision
- Target market
- Key differentiators
- Scraped website data

### products/{product-name}.md
Contains:
- Product overview
- Main features
- Problem solved
- Value proposition
- Competition analysis
- Pricing (if available)

### target-companies.md
Contains:
- Ideal Customer Profile (ICP)
- Company profiles by type (industry, size, characteristics)
- Buying committee roles
- Qualification criteria

### personas/{persona-name}.md
- Role and responsibilities
- Key problems and pain points
- Goals and objectives
- Discovery questions
- Objection handling

### competitors/{competitor}.md
- Competitive battlecards
- Feature comparison and positioning
- When we win / when they win
- Trap-setting questions

### sales-plays/{play}.md
- Trigger signals
- Target personas
- Key messages
- Discovery framework
- Objection handling
- Email templates

## Configuration

The Cursor AI uses these instruction files:
- `.cursor/rules/` - Cursor AI rules (modular format)
- `.cursor/commands/` - Slash commands

## Tips

1. **Be specific** when entering the company name
2. **Use the main website URL** (not subpages)
3. **Review carefully** before confirming - the AI will research based on your approval
4. **Add products manually** if automatic detection misses some
5. **Check scraping.log** to see which URLs were scraped
6. **Load README.md or INDEX.md** when using AI agents for company context

## Web Scraping

Sales Brain uses a Python script for web scraping:

```bash
# Scrape a URL (log to company directory)
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d brains/{company}/

# Scrape and save to JSON file
python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d brains/{company}/ -o output.json
```

**Options:**
- `-d, --log-dir` - Directory for scraping.log (default: current directory)
- `-o, --output` - Save JSON output to file
- `-f, --follow` - Follow discovered links (about, products, pricing, contact, all)
- `-m, --max-pages` - Maximum pages when following links (default: 10)

The script extracts:
- Page title and meta description
- All headings (h1, h2, h3)
- Important links (about, products, pricing, contact)
- Main text content (first 5000 chars)

**Scraping strategy**: The AI will scrape first, then validate with you.

## ⚠️ Disclaimer

**The example company data included in this repository (e.g., `brains/salesloft/`) is for demonstration purposes only.**

- All information was gathered from publicly available sources (company websites, public documentation)
- This data is provided to illustrate how the tool works and what output to expect
- The example sales playbooks, competitive battlecards, and objection handling scripts are samples to demonstrate the framework's capabilities
- **This is not official sales material** from any company mentioned
- Users should generate their own research for actual sales use

The framework, templates, and tooling are the primary value of this project.

## Authors

**Tomas Zeman**  
📧 tomas.zeman@gmail.com

## License

MIT
