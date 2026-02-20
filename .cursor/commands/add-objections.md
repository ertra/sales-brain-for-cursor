# Add Objections

Add objection handling for a specific persona.

## Usage

```
/add objections {company}
```

**Examples:**
- `/add objections outreach` - Add objections for an Outreach persona
- `/add objections gong` - Add objections for a Gong persona

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /add objections {company}

Example: /add objections outreach
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists

2. **List existing personas**:
   - Show personas from `brains/{company}/personas/` directory
   - Ask which persona to add objections for

3. **🔍 SCRAPE** for objections:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://g2.com/products/{company}/reviews -d brains/{company}/
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/faq -d brains/{company}/
   ```

4. **Ask for objection details**:
   - Objection statement (what they say)
   - Category (price, timing, competition, need, authority)
   - Why they say it (underlying concern)
   - How to acknowledge
   - How to respond
   - Proof points to use
   - Prevention strategies

5. **Create `brains/{company}/objections/` directory** if it doesn't exist

6. **Create or update objections file**:
   - Generate `brains/{company}/objections/{persona-slug}-objections.md`
   - Follow the template from `templates/objection-template.md`

7. **Confirm creation**:
   - Show the created file
   - Ask if they want to add more objections

## Template

Use `templates/V1-CONTRACT.md` and `templates/objection-template.md` for structure.
Require frontmatter + `Evidence & Sources` + `Operator Guidance` + `Cross-References`.

## Objection Categories

- **Price**: "Too expensive", "No budget"
- **Timing**: "Not now", "Next quarter"
- **Competition**: "We use X", "Competitor is better"
- **Need**: "We don't need this", "Current solution works"
- **Authority**: "Need to check with...", "Not my decision"
