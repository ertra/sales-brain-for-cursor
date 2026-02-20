# Add Competitor

Add competitive intelligence for a competitor.

## Usage

```
/add competitor {company}
```

**Examples:**
- `/add competitor outreach` - Add competitor to Outreach
- `/add competitor gong` - Add competitor to Gong

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /add competitor {company}

Example: /add competitor outreach
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists

2. **Ask for competitor name and website**

3. **🔍 SCRAPE COMPETITOR WEBSITE DIRECTLY**:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com -d brains/{company}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com/products -d brains/{company}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://competitor.com/pricing -d brains/{company}/
   ```

4. **🔍 SCRAPE comparison pages**:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/vs-competitor -d brains/{company}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/compare/company-vs-competitor -d brains/{company}/
   ```

5. **Ask for competitive details**:
   - Competitor overview
   - Their key products
   - Strengths (where they win)
   - Weaknesses (where we win)
   - Pricing comparison
   - Feature comparison
   - Common objections when competing
   - How to win against them

6. **Create `brains/{company}/competitors/` directory** if it doesn't exist

7. **Create competitor file**:
   - Generate `brains/{company}/competitors/{competitor-slug}.md`
   - Follow the template from `templates/competitor-template.md`

8. **Confirm creation**:
   - Show the competitive battlecard
   - Ask if they want to add more competitors

## Template

Use `templates/V1-CONTRACT.md` and `templates/competitor-template.md` for structure.
Require frontmatter + `Evidence & Sources` + `Operator Guidance` + `Cross-References`.

## Important

- **SCRAPE COMPETITOR WEBSITES DIRECTLY** for accurate info
- Don't rely only on your company's "vs" pages
- G2 comparisons provide real user feedback
