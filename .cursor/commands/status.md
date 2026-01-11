# Sales Brain Status

Show the current progress and freshness of sales intelligence for a company.

## Usage

```
/status {company}
```

If no company specified, list all available companies.

## What to Show

### 1. Phase Completion Status

Check which phases are complete by looking for files:

```
🧠 Sales Brain Status: Outreach

Phase Completion:
✅ Phase 1: Company Research    - company.md
✅ Phase 2: Products            - 7 products
✅ Phase 3: Target Companies    - target-companies.md
✅ Phase 4: Personas            - 6 personas
✅ Phase 5: Pain Points         - 6 files
✅ Phase 6: Value Propositions  - 7 files
✅ Phase 7: Use Cases           - 4 files
✅ Phase 8: Competitors         - 3 files
✅ Phase 9: Objections          - 6 files
✅ Phase 10: Case Studies       - 5 files
✅ Phase 11: Sales Plays        - 4 files

Progress: 11/11 phases complete ████████████ 100%
```

### 2. Freshness Indicators 🕐

Check file modification dates and show freshness:

```
📅 Freshness Report:

| File/Section | Last Updated | Status |
|--------------|--------------|--------|
| company.md | 2 days ago | 🟢 Fresh |
| products/ | 2 days ago | 🟢 Fresh |
| target-companies.md | 2 days ago | 🟢 Fresh |
| personas/ | 2 days ago | 🟢 Fresh |
| pain-points/ | 2 days ago | 🟢 Fresh |
| value-propositions/ | 2 days ago | 🟢 Fresh |
| use-cases/ | 2 days ago | 🟢 Fresh |
| competitors/ | 2 days ago | 🟢 Fresh |
| objections/ | 2 days ago | 🟢 Fresh |
| case-studies/ | 2 days ago | 🟢 Fresh |
| sales-plays/ | 2 days ago | 🟢 Fresh |
```

### Freshness Rules

| Age | Status | Meaning |
|-----|--------|---------|
| < 7 days | 🟢 Fresh | Recently updated |
| 7-30 days | 🟡 Aging | Consider reviewing |
| 30-90 days | 🟠 Stale | Should be updated |
| > 90 days | 🔴 Outdated | Needs immediate refresh |

### 3. File Statistics

```
📊 Statistics:

Total files: 54
Total content: ~45,000 words

By type:
- Products: 7 files
- Personas: 6 files
- Pain Points: 6 files
- Value Propositions: 7 files
- Use Cases: 4 files
- Competitors: 3 files
- Objections: 6 files
- Case Studies: 5 files
- Sales Plays: 4 files
```

### 4. Scraping Stats (if available)

Check `scraping.txt` and `scraping.log`:

```
🔍 Scraping Stats:

Pages scraped: 47
Last scrape: 2 days ago

Recent URLs:
- https://outreach.io/products
- https://outreach.io/customers
- https://g2.com/products/outreach/reviews
- https://salesloft.com
- https://gong.io
```

### 5. Recommendations

Based on freshness and completion:

```
💡 Recommendations:

1. 🟠 competitors/gong.md is 45 days old - consider refreshing
2. ⬚ No sales plays for "New Logo" scenario - consider adding
3. 🟡 Case studies section has only 5 entries - add more social proof
```

## How to Get File Dates

Use terminal commands to check modification dates:

```bash
# Get modification date of a file
stat -f "%Sm" {company}/company.md

# List all files with dates
find {company}/ -name "*.md" -exec stat -f "%Sm %N" {} \;

# Or on Linux:
find {company}/ -name "*.md" -printf "%T+ %p\n" | sort -r
```

## No Company Specified

If user runs `/status` without a company:

```
🧠 Sales Brain - Available Companies

Found 2 company directories:

1. outreach/
   - 11/11 phases complete
   - Last updated: 2 days ago
   - 54 files

2. gong/
   - 4/11 phases complete
   - Last updated: 5 days ago
   - 12 files

Use /status {company} for detailed status.
Use /continue {company} to continue a workflow.
```

## Company Not Found

```
❌ Company '{company}' not found.

Available companies:
- outreach
- gong

Use /start to begin a new company.
```
