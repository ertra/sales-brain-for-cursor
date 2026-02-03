# Add Sales Play

Add an actionable sales playbook.

## Usage

```
/add sales-play {company}
```

**Examples:**
- `/add sales-play outreach` - Add sales play for Outreach
- `/add sales-play gong` - Add sales play for Gong

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /add sales-play {company}

Example: /add sales-play outreach
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists

2. **Review existing content**:
   - Products available
   - Personas documented
   - Pain points identified
   - Value propositions created
   - Competitors analyzed
   - Case studies available

3. **Ask for sales play details**:
   - Play name (e.g., "Competitive Displacement - Gong")
   - When to run this play (trigger events)
   - Target persona
   - Target company profile
   - Execution steps
   - Talk track / messaging
   - Discovery questions
   - Demo flow
   - Objection handling
   - Success metrics
   - Required materials

4. **Create `brains/{company}/sales-plays/` directory** if it doesn't exist

5. **Create sales play file**:
   - Generate `brains/{company}/sales-plays/{play-slug}.md`
   - Follow the template from `templates/sales-play-template.md`

6. **Confirm creation**:
   - Show the created playbook
   - Ask if they want to add more plays

## Template

Use `templates/sales-play-template.md` for structure.

## Common Sales Play Types

- **Competitive Displacement** - Win against specific competitor
- **New Logo** - Land new customers
- **Expansion** - Grow existing accounts
- **Platform Consolidation** - Replace point solutions
- **Executive Alignment** - Engage C-suite
- **Renewal** - Retain and grow at renewal
- **Trigger Event** - Respond to news/events
