# Generate Summary

Generate or regenerate the SUMMARY.md file for a company's sales brain.

## Usage

```
/generate-summary {company}
```

**Examples:**
- `/generate-summary outreach` - Generate summary for Outreach
- `/generate-summary gong` - Generate summary for Gong

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /generate-summary {company}

Example: /generate-summary outreach
```

## What It Does

Scans all files in the company directory and creates a condensed `{company}/SUMMARY.md` (~1000 tokens) with key information from all sources.

## Workflow Steps

### Step 1: Verify Company Exists
Check if `{company}/` directory exists.

### Step 2: Extract Information

Read and extract key info from each file type:

#### From company.md
- Company name
- One-line description
- Website
- Key differentiators (bullet points)

#### From products/*.md
- Product name
- One-line description of what it does

#### From target-companies.md
- Target company types
- Industries
- Company characteristics

#### From personas/*.md
- Persona name/title
- Key pain point (most important one)
- Key value we provide

#### From competitors/*.md
- Competitor name
- Their main strength
- Our advantage against them

#### From objections/*.md (most common ones)
- Top 5-6 objections across all personas
- Quick response for each

#### From case-studies/*.md
- Customer name
- Key metric/result

#### From sales-plays/*.md
- Play name
- When to use it (trigger)

### Step 3: Generate SUMMARY.md

Use this template structure:

```markdown
# {Company} - Quick Context (~1000 tokens)

**Always load this file for any {Company}-related conversation.**

## Company
{One paragraph description from company.md}

## Products ({count})
| Product | What It Does |
|---------|--------------|
| **{Product 1}** | {One-line description} |
| **{Product 2}** | {One-line description} |
...

## Target Companies
- **{Type 1}** ({size})
- **Industries**: {list}
- **Characteristics**: {key traits}

## Personas ({count})
| Persona | Key Pain | Our Value |
|---------|----------|-----------|
| **{Persona 1}** | {Main problem} | {How we help} |
| **{Persona 2}** | {Main problem} | {How we help} |
...

## Top Competitors
| Competitor | Their Strength | Our Advantage |
|------------|----------------|---------------|
| **{Competitor 1}** | {What they do well} | {Why we win} |
...

## Common Objections (Quick Responses)
| Objection | Response |
|-----------|----------|
| "{Objection 1}" | {Brief response} |
| "{Objection 2}" | {Brief response} |
...

## Proof Points (Metrics)
- **{Customer 1}**: {Key result}
- **{Customer 2}**: {Key result}
...

## Key Differentiators
1. {Differentiator 1}
2. {Differentiator 2}
...

## Sales Plays (When to Use)
| Situation | Play |
|-----------|------|
| {Trigger 1} | `sales-plays/{play-1}.md` |
| {Trigger 2} | `sales-plays/{play-2}.md` |
...

---
*Load full files from INDEX.md when deeper context needed.*
```

### Step 4: Save SUMMARY.md
Write to `{company}/SUMMARY.md`

### Step 5: Confirm Creation
Show:
- Token estimate
- What was included
- Any missing sections

## Extraction Tips

### Getting One-Liners
When extracting from files, take only:
- First sentence of Overview section
- First bullet point of key sections
- Most impactful metric from case studies

### Keeping It Short
- Products: Max 10 words per description
- Personas: Max 8 words for pain, 8 for value
- Objections: Max 15 words for response
- Proof points: Just customer + one metric

### Prioritization
If too many items, prioritize:
- Products: Top 7-8 by importance
- Personas: All (usually 5-7)
- Competitors: Top 3
- Objections: Top 6 (most common)
- Case studies: Top 5 with best metrics
- Sales plays: All (usually 3-5)

## Output Example

```
✅ Generated SUMMARY.md for Outreach

📊 Summary Statistics:
- Company: ✓ extracted
- Products: 7 included
- Target Companies: ✓ extracted
- Personas: 6 included
- Competitors: 3 included
- Objections: 6 included
- Proof Points: 5 included
- Sales Plays: 4 included

💾 Estimated Size: ~950 tokens

Location: outreach/SUMMARY.md
```

## When to Run

- After `/start` workflow completes (with INDEX.md)
- After `/refresh` completes
- After adding significant new content
- Manually anytime with `/generate-summary {company}`

## Error Handling

### Missing Files
If some files don't exist, skip that section and note it:
```
⚠️ Missing sections (not included in summary):
- competitors/ - No competitor files found
- case-studies/ - No case study files found

Consider adding these with:
- /add competitor {company}
- /add case-study {company}
```

### File Reading Errors
If a file can't be read, skip it and continue with others.
