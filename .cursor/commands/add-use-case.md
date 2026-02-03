# Add Use Case

Add a use case scenario combining products, personas, and target companies.

## Usage

```
/add use-case {company}
```

**Examples:**
- `/add use-case outreach` - Add use case for Outreach
- `/add use-case gong` - Add use case for Gong

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /add use-case {company}

Example: /add use-case outreach
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists

2. **🔍 SCRAPE** for use cases:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/use-cases
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/solutions
   ```

3. **Ask for use case details**:
   - Use case name/title
   - Context and trigger events (what happens to trigger need)
   - Target company profile
   - Target persona
   - The challenge they face
   - The solution (which products)
   - Before state vs After state
   - Value delivered
   - Proof points

4. **Create `brains/{company}/use-cases/` directory** if it doesn't exist

5. **Create use case file**:
   - Generate `brains/{company}/use-cases/{use-case-slug}.md`
   - Follow the template from `templates/use-case-template.md`

6. **Confirm creation**:
   - Show the created file
   - Ask if they want to add more use cases

## Template

Use `templates/use-case-template.md` for structure.
