# Generate Visualization

Generate an interactive HTML visualization of the sales brain knowledge graph.

## Usage

```
/generate-visualization {company}
```

**Example:** `/generate-visualization outreach`

## Required Parameter

**Company name is required.**

## What It Does

Scans all files in `brains/{company}/` and generates `brains/{company}/visualization.html` - an interactive force-directed graph showing:

1. **All sales objects as nodes** with type-based colors
2. **Relationships as edges** showing connections
3. **Interactive features**: click, zoom, pan, search, filter

## Node Types & Colors

| Type | Color | Icon |
|------|-------|------|
| Company | Cyan | 🏢 |
| Product | Blue | 📦 |
| Persona | Green | 👤 |
| Pain Point | Yellow | 😣 |
| Value Prop | Purple | 💎 |
| Competitor | Red | ⚔️ |
| Use Case | Orange | 📋 |
| Case Study | Pink | 📈 |
| Sales Play | Indigo | 🎯 |

## Relationships Shown

```
Company → Products (offers)
Products → Personas (serves)
Personas → Pain Points (experiences)
Products → Value Props (delivers)
Value Props → Personas (for)
Company → Competitors (competes)
Products → Use Cases (enables)
Use Cases → Personas (for)
Company → Case Studies (proves)
```

## Features

### 1. Filter by Type
Toggle visibility of node types using sidebar buttons.

### 2. Search
Type to filter nodes by name or description.

### 3. Node Details
Click any node to see:
- Description
- Connected nodes
- Source file path

### 4. Navigation
- Zoom: scroll wheel
- Pan: click and drag
- Focus: click node
- Fit: fit button
- Reset: reset button

## Data Extraction

When generating, read from markdown files:

```python
# Pseudocode for extraction
for file in company_dir:
    if file.endswith('.md'):
        extract:
            - id (from filename)
            - name (from # heading)
            - description (from ## Overview or first paragraph)
            - type (from directory)
            - relationships (from ## sections)
```

## Output

Single self-contained HTML file:
- No external dependencies (vis.js loaded from CDN)
- Dark theme with modern UI
- Responsive sidebar with stats
- Works in any browser

## When to Run

- After `/start` workflow completes
- After adding significant new objects
- When you want to review relationships
- For presentations or documentation
