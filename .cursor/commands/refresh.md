# Refresh Sales Brain

Refresh and update all sales intelligence for a company when web content has changed.

## Usage

```
/refresh {company}
```

**Examples:**
- `/refresh outreach` - Refresh all Outreach content
- `/refresh gong` - Refresh all Gong content

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /refresh {company}

Example: /refresh outreach
```

## Refresh Workflow

### Step 1: Ask What's New 🆕

Before scraping, ask the user what has changed:

```
🔄 Refreshing Outreach

Before I start scraping, please tell me:

1. **What's new or changed?** (optional - helps me focus)
   Examples:
   - "New product launched"
   - "Pricing changed"
   - "New competitor entered market"
   - "Company raised funding"
   - "New case studies published"

2. **Any new URLs to add?** (optional)
   Current sources in scraping.log: 47 URLs
   
   Add new URLs to scrape? (paste URLs, one per line, or "none")

Your answer:
```

### Step 2: Review Existing URLs

Show the user what URLs are in `scraping.log`:

```
📋 Current Scraping Sources (from scraping.log):

Company:
- https://outreach.io
- https://outreach.io/about

Products:
- https://outreach.io/products
- https://outreach.io/platform
- https://outreach.io/pricing

Competitors:
- https://gong.io
- https://salesloft.com
- https://clari.com

Reviews:
- https://g2.com/products/outreach/reviews

Total: 47 URLs

Add more URLs? (paste below, or "continue" to proceed)
```

### Step 3: Scrape All Sources

Re-scrape all URLs using Python script:

```bash
# Scrape each URL from scraping.log
python .cursor/rules/sales-brain/scripts/scrape.py scrape https://outreach.io
python .cursor/rules/sales-brain/scripts/scrape.py scrape https://outreach.io/products
# ... etc
```

Show progress:
```
🔍 Scraping sources...

[1/47] https://outreach.io ✅
[2/47] https://outreach.io/about ✅
[3/47] https://outreach.io/products ✅
[4/47] https://gong.io ✅
...
[47/47] https://g2.com/products/outreach/reviews ✅

Scraping complete! Analyzing changes...
```

### Step 4: Analyze & Show Changes

Compare scraped content with existing files:

```
📊 Changes Detected:

| Section | Status | What Changed |
|---------|--------|--------------|
| company.md | 🟡 Update | New funding info, employee count |
| products/ | 🔴 Major | New product "Kaia" discovered |
| target-companies.md | 🟢 Current | No changes |
| personas/ | 🟢 Current | No changes |
| pain-points/ | 🟡 Update | New pain points from G2 reviews |
| value-propositions/ | 🟢 Current | No changes |
| use-cases/ | 🟢 Current | No changes |
| competitors/gong.md | 🟡 Update | New pricing structure |
| competitors/salesloft.md | 🟢 Current | No changes |
| objections/ | 🟡 Update | New objections from reviews |
| case-studies/ | 🔴 Major | 3 new case studies found |
| sales-plays/ | 🟢 Current | No changes |

Legend:
🟢 Current - No changes needed
🟡 Update - Minor updates available
🔴 Major - Significant new content
```

### Step 5: Choose What to Update

```
🔄 Update Options:

1. Update ALL changed sections (5 sections)
2. Update only MAJOR changes (2 sections)
3. Select specific sections to update
4. Review changes in detail first
5. Skip - don't update anything

What would you like to do? (1-5)
```

If user chooses to review:
```
📝 Detailed Changes:

## company.md
- Found: "Series D funding of $200M" (new)
- Found: "1,200+ employees" (was 1,000+)

## products/
- NEW PRODUCT: "Kaia" - AI meeting assistant
- Updated: Sales Engagement - new feature "Smart Email"

## case-studies/
- NEW: "Zoom Customer Story"
- NEW: "Snowflake Success"  
- NEW: "Databricks Case Study"

Update these? (yes/no/select)
```

### Step 6: Apply Updates

For each section to update:
1. Read current file
2. Merge new information (don't lose existing content)
3. Save updated file
4. Show what was updated

```
✅ Updates Applied:

- company.md - Updated funding and employee count
- products/kaia.md - Created new product file
- pain-points/sdr-bdr-pain-points.md - Added 2 new pain points
- competitors/gong.md - Updated pricing section
- case-studies/zoom.md - Created new case study
- case-studies/snowflake.md - Created new case study
- case-studies/databricks.md - Created new case study

📊 Summary:
- Files updated: 4
- Files created: 4
- Sections refreshed: 5

Last refresh: 2026-01-10 22:30
```

### Step 7: Update Scraping Log

Add any new URLs to `scraping.log` with timestamp.

### Step 8: Regenerate INDEX.md

After all updates are applied, regenerate the INDEX.md file:

1. Scan all files in `brains/{company}/` directory
2. Update file counts and descriptions
3. Update "Last generated" timestamp
4. Show confirmation

```
✅ INDEX.md regenerated

Updated sections:
- Products: 7 → 8 files (new: kaia.md)
- Case Studies: 5 → 8 files (3 new)
```

## Error Handling

### No scraping.log found
```
⚠️ No scraping.log found for Outreach.

This means no previous URLs were tracked. 

Options:
1. Start fresh - I'll scrape the main website and discover URLs
2. Provide URLs manually

What would you like to do?
```

### Scraping failures
```
⚠️ Some URLs failed to scrape:

❌ https://g2.com/products/outreach/reviews - 403 Forbidden
❌ https://oldurl.com/page - 404 Not Found

Continue with successful scrapes? (yes/no)
```

## Quick Refresh Mode

If user just wants a quick refresh without prompts:

```
/refresh outreach --quick
```

This will:
1. Scrape all URLs from scraping.log
2. Auto-update all changed sections
3. Show summary at end

## Refresh Specific Section

To refresh only one section:

```
/refresh outreach --section competitors
/refresh outreach --section products
/refresh outreach --section case-studies
```
