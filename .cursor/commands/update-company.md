# Update Company

Re-research and update company information.

## Usage

```
/update company {company}
```

**Examples:**
- `/update company outreach` - Update Outreach company info
- `/update company gong` - Update Gong company info

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /update company {company}

Example: /update company outreach

Available companies:
- outreach
- gong
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `{company}/company.md` exists
   - If not, suggest `/start` to create company first

2. **Read existing company.md**:
   - Show current information
   - Ask what needs to be updated

3. **🔍 SCRAPE** for fresh information:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/about
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/company
   ```

4. **Compare and show changes**:
   - Highlight what's new or different
   - Ask user to confirm updates

5. **Update `{company}/company.md`**:
   - Merge new information
   - Preserve user-added notes
   - Update timestamp

6. **Confirm update**:
   - Show updated file
   - Offer to update other sections

## What Gets Updated

- Company overview/description
- Employee count
- Headquarters
- Funding information
- Mission/vision statements
- Key differentiators
- Recent news

## Note

For a full refresh of all content, use `/refresh {company}` instead.
