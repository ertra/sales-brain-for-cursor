# Add Persona

Add a new persona to a company's personas directory.

## Usage

```
/add persona {company}
```

**Examples:**
- `/add persona outreach` - Add persona to Outreach
- `/add persona gong` - Add persona to Gong

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /add persona {company}

Example: /add persona outreach

Available companies:
- outreach
- gong
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists
   - If not, suggest `/start` to create company first

2. **Ask for persona information**:
   - Persona name/title (required)
   - Role and responsibilities
   - Company profile (type of company they work for - generic)
   - Key problems and pain points
   - Goals and objectives
   - How the company's products solve their problems
   - Buying process
   - Communication preferences

3. **🔍 SCRAPE** if persona page exists:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/solutions/for-sales-leaders
   ```

4. **Create `brains/{company}/personas/` directory** if it doesn't exist

5. **Create persona file**:
   - Generate `brains/{company}/personas/{persona-slug}.md` following the template
   - **IMPORTANT**: Do NOT include a "Company" field - personas are generic

6. **Confirm creation**:
   - Show the created persona file
   - Ask if they want to add pain points for this persona

## Important

- Personas are GENERIC - they work for any target company
- Do NOT include a specific "Company" field in the persona file
- Use `templates/persona-template.md` for structure
