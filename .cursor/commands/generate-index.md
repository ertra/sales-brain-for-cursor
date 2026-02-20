# Generate Index

Generate or regenerate the INDEX.md file for a company's sales brain.

## Usage

```
/generate-index {company}
```

**Examples:**
- `/generate-index outreach` - Generate index for Outreach
- `/generate-index gong` - Generate index for Gong

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /generate-index {company}

Example: /generate-index outreach
```

## What It Does

Scans the company directory and creates/updates `brains/{company}/INDEX.md` with:

1. **Quick Reference** - Company name, website, main products
2. **File Inventory** - List of all .md files organized by category
3. **Loading Rules** - Instructions for AI agents on when to load each file
4. **Topic Mapping** - Keywords that should trigger loading specific files
5. **V1 Coverage Check** - Which files are V2-compliant vs pending migration

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists

2. **Scan directory structure**:
   - Count files in each subdirectory
   - Extract key info from company.md
   - List all products, personas, competitors, etc.

3. **Generate INDEX.md content**:

```markdown
# {Company} Sales Brain Index

## Quick Reference
- **Company**: {extracted from company.md}
- **Website**: {URL}
- **Main Products**: {list from products/}

## Available Context Files

### Always Relevant
- `company.md` - Company overview
- `target-companies.md` - Target customer profiles

### Products ({count} files)
Load when user asks about specific product:
{list each product file with 1-line description}

### Personas ({count} files)
Load when discussing specific role:
{list each persona file}

### Pain Points ({count} files)
{list files}

### Value Propositions ({count} files)
{list files}

### Use Cases ({count} files)
{list files}

### Competitors ({count} files)
Load when competitor mentioned:
{list files}

### Objections ({count} files)
Load when handling pushback:
{list files}

### Case Studies ({count} files)
Load when need proof points:
{list files}

### Sales Plays ({count} files)
Load for specific sales motions:
{list files}

## Loading Rules for AI Agent

1. **Always load**: INDEX.md (this file)
2. **Detect topic** from user query and load relevant files
3. **Use search** when unsure

## Topic → File Mapping

| User Mentions | Load These Files |
|---------------|------------------|
| Product name | That product file |
| Persona/role | Persona + pain points + objections |
| Competitor name | Competitor battlecard |
| "objection", "pushback" | Relevant objection files |
| "proof", "customer", "case study" | Case study files |
| "pitch", "value", "message" | Value proposition files |
| "play", "strategy" | Sales play files |

## Statistics
- Total files: {count}
- Last generated: {timestamp}
```

4. **Save INDEX.md**:
   - Write to `brains/{company}/INDEX.md`

5. **Confirm creation**:
   - Show summary of what was indexed
   - Show file counts by category

## When to Run

- Automatically after `/start` workflow completes (Phase 11)
- Automatically after `/refresh` completes
- Manually anytime with `/generate-index {company}`
- After adding new files with `/add` commands

## Output Example

```
✅ Generated INDEX.md for Outreach

📊 Indexed:
- Products: 7 files
- Personas: 6 files
- Pain Points: 6 files
- Value Propositions: 7 files
- Use Cases: 4 files
- Competitors: 3 files
- Objections: 6 files
- Case Studies: 5 files
- Sales Plays: 4 files

Total: 54 files indexed
Location: brains/outreach/INDEX.md
```
