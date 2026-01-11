# Add Product

Add a new product to a company's products directory.

## Usage

```
/add product {company}
```

**Examples:**
- `/add product outreach` - Add product to Outreach
- `/add product gong` - Add product to Gong

## Required Parameter

**Company name is required.**

If missing:
```
❌ Please specify the company name.

Usage: /add product {company}

Example: /add product outreach

Available companies:
- outreach
- gong
```

## Workflow Steps

1. **Verify company exists**:
   - Check if `{company}/` directory exists
   - If not, suggest `/start` to create company first

2. **Ask for product information**:
   - Product name (required)
   - Product description/overview
   - Main features
   - Problem it solves
   - Value proposition
   - Target customers
   - Any known competitors

3. **🔍 SCRAPE** product page if URL provided:
   ```bash
   python .cursor/rules/sales-brain/scripts/scrape.py scrape https://company.com/products/new-product
   ```

4. **Create `{company}/products/` directory** if it doesn't exist

5. **Create product file**:
   - Generate `{company}/products/{product-slug}.md` following the template
   - Use the product name to create a URL-friendly slug
   - Fill in all provided information

6. **Confirm creation**:
   - Show the created product file
   - Ask if they want to add more products or make changes

## Template

Use the product template from `templates/` directory.
