# Add Case Study

Add a customer success story.

## Usage

```
/add case-study {company}
```

**Examples:**
- `/add case-study outreach` - Add case study for Outreach
- `/add case-study gong` - Add case study for Gong

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /add case-study {company}

Example: /add case-study outreach
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists

2. **🔍 SCRAPE** customer stories:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/customers
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/case-studies/{customer}
   ```

3. **Ask for case study details**:
   - Customer name
   - Industry and company size
   - Challenge they faced
   - Which personas were involved
   - Solution implemented (which products)
   - Results achieved (with metrics)
   - Timeline
   - Quotes from customer
   - Related use cases

4. **Create `brains/{company}/case-studies/` directory** if it doesn't exist

5. **Create case study file**:
   - Generate `brains/{company}/case-studies/{customer-slug}.md`
   - Follow the template from `templates/case-study-template.md`

6. **Confirm creation**:
   - Show the created file
   - Ask if they want to add more case studies

## Template

Use `templates/case-study-template.md` for structure.

## Important

- Include specific METRICS (%, $, time saved)
- Include direct QUOTES from customers
- Tag with relevant personas and products
- Great case studies prove ROI
