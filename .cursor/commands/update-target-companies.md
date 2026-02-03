# Update Target Companies

Update target companies information.

## Usage

```
/update target-companies {company}
```

**Examples:**
- `/update target-companies outreach` - Update Outreach target companies
- `/update target-companies gong` - Update Gong target companies

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /update target-companies {company}

Example: /update target-companies outreach

Available companies:
- outreach
- gong
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists
   - If not, suggest `/start` to create company first

2. **Read existing target-companies.md** (if exists):
   - Show current target company profiles
   - Ask what needs to be updated or added

3. **🔍 SCRAPE** for target company info:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/customers
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/industries
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/case-studies
   ```

4. **Ask for updates**:
   - New company types to add?
   - Changes to existing profiles?
   - New industries to target?
   - Updated characteristics?

5. **Update `brains/{company}/target-companies.md`**:
   - Merge new information
   - Preserve existing profiles
   - Add new profiles

6. **Confirm update**:
   - Show updated file
   - Suggest reviewing personas if target companies changed significantly
