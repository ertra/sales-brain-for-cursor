# Search Sales Brain

Search across all sales intelligence files for a specific term or topic.

## Usage

```
/search {company} {query}
```

**Examples:**
- `/search outreach pricing objection` - Find mentions of pricing objections
- `/search outreach CRO` - Find all CRO-related content
- `/search outreach competitor Gong` - Find Gong competitor info

## Required Parameters

1. **Company name** - Which company's files to search
2. **Search query** - What to look for

If parameters are missing:
```
❌ Please specify company and search term.

Usage: /search {company} {query}

Example: /search outreach pricing objection
```

## How to Search

### Step 1: Validate Company Exists

Check if `brains/{company-slug}/` directory exists.

### Step 2: Search All Markdown Files

Use grep to search across all `.md` files in the company directory:

```bash
grep -r -i -n "{query}" brains/{company-slug}/ --include="*.md"
```

Or search with context:
```bash
grep -r -i -n -C 3 "{query}" brains/{company-slug}/ --include="*.md"
```

### Step 3: Present Results

Group results by file type and show relevant snippets:

```
🔍 Search Results for "pricing" in Outreach

📁 objections/cro-objections.md (3 matches)
   Line 45: "Your pricing is too high compared to..."
   Line 67: "We need to understand the pricing model..."
   Line 89: "Pricing concern: Show ROI calculator..."

📁 competitors/salesloft.md (2 matches)
   Line 23: "Pricing: Salesloft is typically 15% cheaper..."
   Line 56: "Counter pricing objection with value story..."

📁 value-propositions/platform-revops.md (1 match)
   Line 34: "Pricing consolidation saves 30% vs point solutions..."

Total: 6 matches in 3 files
```

### Step 4: Offer Follow-up Actions

After showing results, offer:
- "Would you like me to read any of these files in full?"
- "Would you like me to summarize the findings?"
- "Would you like to search for something else?"

## Search Tips

| Query Type | Example | Finds |
|------------|---------|-------|
| Single word | `/search outreach ROI` | All ROI mentions |
| Phrase | `/search outreach "pricing objection"` | Exact phrase |
| Persona | `/search outreach CRO` | CRO-related content |
| Competitor | `/search outreach Gong` | Gong mentions |
| Topic | `/search outreach forecast` | Forecasting content |

## Q&A Mode

For question-style searches, interpret the intent:

| User Says | Search For |
|-----------|------------|
| "What objections does a CRO raise?" | Search objections/cro-objections.md |
| "How do we compete with Gong?" | Search competitors/gong.md |
| "What pain points do SDRs have?" | Search pain-points/sdr-*.md |
| "What's our value prop for AEs?" | Search value-propositions/*-ae.md |

## No Results

If no results found:
```
🔍 No results for "xyz" in Outreach

Suggestions:
- Try a different term
- Check spelling
- Use broader search terms

Available files to search:
- 7 products
- 6 personas
- 6 pain-points files
- 7 value-propositions
- 4 use-cases
- 3 competitors
- 6 objections files
- 5 case-studies
- 4 sales-plays
```
