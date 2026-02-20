# Add Pain Points

Add pain points for a specific persona.

## Usage

```
/add pain-points {company}
```

**Examples:**
- `/add pain-points outreach` - Add pain points for an Outreach persona
- `/add pain-points gong` - Add pain points for a Gong persona

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /add pain-points {company}

Example: /add pain-points outreach
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists
   - If not, suggest `/start` to create company first

2. **List existing personas**:
   - Show personas from `brains/{company}/personas/` directory
   - Ask which persona to add pain points for

3. **🔍 SCRAPE** for pain points:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/products/{company}/reviews -d brains/{company}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/challenges -d brains/{company}/
   ```

4. **Ask for pain point details**:
   - Pain point description
   - Impact (high/medium/low)
   - Frequency (daily/weekly/monthly)
   - Current solutions they use
   - Which products address this pain point
   - Discovery questions to uncover this pain

5. **Create `brains/{company}/pain-points/` directory** if it doesn't exist

6. **Create or update pain points file**:
   - Generate `brains/{company}/pain-points/{persona-slug}-pain-points.md`
   - Follow the template from `templates/pain-points-template.md`

7. **Confirm creation**:
   - Show the created file
   - Ask if they want to add more pain points

## Template

Use `templates/V1-CONTRACT.md` and `templates/pain-points-template.md` for structure.
Require frontmatter + `Evidence & Sources` + `Operator Guidance` + `Cross-References`.
