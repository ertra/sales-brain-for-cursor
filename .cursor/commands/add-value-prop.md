# Add Value Proposition

Add a value proposition for a product-persona combination.

## Usage

```
/add value-prop {company}
```

**Examples:**
- `/add value-prop outreach` - Add value prop for Outreach
- `/add value-prop gong` - Add value prop for Gong

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /add value-prop {company}

Example: /add value-prop outreach
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists

2. **List existing products**:
   - Show products from `brains/{company}/products/` directory
   - Ask which product

3. **List existing personas**:
   - Show personas from `brains/{company}/personas/` directory
   - Ask which persona

4. **🔍 SCRAPE** for value messaging:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/roi
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/value
   ```

5. **Ask for value proposition details**:
   - Core problem solved for this persona
   - Key value drivers
   - Quantified benefits (metrics, percentages)
   - ROI story
   - Messaging framework (headlines, taglines)
   - Proof points

6. **Create `brains/{company}/value-propositions/` directory** if it doesn't exist

7. **Create value proposition file**:
   - Generate `brains/{company}/value-propositions/{product-slug}-{persona-slug}.md`
   - Follow the template from `templates/value-proposition-template.md`

8. **Confirm creation**:
   - Show the created file
   - Suggest related value props to create

## Template

Use `templates/value-proposition-template.md` for structure.
