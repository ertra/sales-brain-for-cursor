# List Products

List all documented products for a specific company.

## Usage

```
/list products {company}
```

**Examples:**
- `/list products outreach` - List Outreach products
- `/list products gong` - List Gong products

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /list products {company}

Example: /list products outreach

Available companies:
- outreach
- gong
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `brains/{company}/` directory exists
   - If not, show available companies

2. **Check for `brains/{company}/products/` directory**:
   - If it doesn't exist, inform the user that no products have been added yet
   - Suggest using `/add product {company}` or `/continue {company}` to add products

3. **List all product files**:
   - Read all `.md` files in the `brains/{company}/products/` directory
   - Extract product names and basic info from each file

4. **Display product summary**:
   ```
   📦 Products for Outreach (7 products)

   1. Sales Engagement
      Platform for automated outreach sequences
      → brains/outreach/products/sales-engagement.md

   2. AI Agents
      Autonomous AI for sales workflows
      → brains/outreach/products/ai-agents.md

   ...
   ```

5. **Offer next steps**:
   - Option to view details of a specific product
   - Option to add more products with `/add product {company}`
   - Option to update existing products
