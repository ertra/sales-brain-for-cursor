# List Personas

List all documented personas for a specific company.

## Usage

```
/list personas {company}
```

**Examples:**
- `/list personas outreach` - List Outreach personas
- `/list personas gong` - List Gong personas

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /list personas {company}

Example: /list personas outreach

Available companies:
- outreach
- gong
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `{company}/` directory exists
   - If not, show available companies

2. **Check for `{company}/personas/` directory**:
   - If it doesn't exist, inform the user that no personas have been added yet
   - Suggest using `/add persona {company}` or `/continue {company}` to add personas

3. **List all persona files**:
   - Read all `.md` files in the `{company}/personas/` directory
   - Extract persona names and basic info from each file

4. **Display persona summary**:
   ```
   👤 Personas for Outreach (6 personas)

   1. SDR/BDR
      Sales Development Representative
      Key problems: Not enough pipeline, manual prospecting
      → outreach/personas/sdr-bdr.md

   2. Account Executive
      Quota-carrying sales rep
      Key problems: Deal visibility, forecast accuracy
      → outreach/personas/account-executive.md

   ...
   ```

5. **Offer next steps**:
   - Option to view details of a specific persona
   - Option to add more personas with `/add persona {company}`
   - Option to see pain points for a persona
