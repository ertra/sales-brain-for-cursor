# LAUTIE Sales Intelligence Index

## Quick Reference

| What You Need | Where to Find It |
|---------------|------------------|
| Company Overview | `company.md` |
| Product Details | `products/` |
| Target Customers / Segments | `target-companies.md` |
| Buyer Personas | `personas/` |
| Pain Points | `pain-points/` |
| Value Props | `value-propositions/` |
| Use Cases | `use-cases/` |
| Competitors | `competitors/` |
| Objection Handling | `objections/` |
| Case Studies | `case-studies/` |
| Sales Plays | `sales-plays/` |

---

## File Inventory

### Core Files
| File | Description |
|------|-------------|
| `company.md` | Company overview, mission, differentiators, website |
| `target-companies.md` | Customer segments (enthusiast, collector, gift, B2B potential) |
| `README.md` | Folder overview (GitHub default) |

### Products (`products/`)
| File | Description |
|------|-------------|
| `fidget-spinners.md` | Noiz, Bit, Carnival, Jackpot, etc. |
| `fidget-sliders.md` | Choc, Shuffle KK/V3, X-Lock 2.0, haptic coins |
| `fidget-rings.md` | Mechanic series (C, E, I, Thorns, A), Noiz-C, Sam-Ring |
| `pendants.md` | Resistor, Capsule, Sugar Cube, Pointer, GAS, etc. |
| `edc-accessories.md` | Pouches, Leather Scroll, BeetleCrash, Watch Buckle, CRANE |
| `diy-accessories.md` | Bearings, Paracord, Polishing Tool, Patch, PELICAN case |

### Personas (`personas/`)
| File | Description |
|------|-------------|
| `fidget-enthusiast.md` | Primary D2C; desk/pocket/wearable fidget |
| `collector.md` | Limited editions, co-brands, series |
| `gift-buyer.md` | Occasion-driven; thoughtful gift |
| `corporate-gift-buyer.md` | B2B potential; HR/wellness/employee gifts |

### Pain Points (`pain-points/`)
| File | Description |
|------|-------------|
| `fidget-enthusiast-pain-points.md` | Cheap breaks, need discreet, choice overload, identity |
| `collector-pain-points.md` | Miss drops, timing, shipping/cost, prioritize |
| `gift-buyer-pain-points.md` | Which type, budget vs premium, delivery, justify gift |
| `corporate-gift-buyer-pain-points.md` | No B2B path, delivery, match to audience, budget/custom |

### Value Propositions (`value-propositions/`)
| File | Description |
|------|-------------|
| `platform-value-prop.md` | Full LAUTIE value prop; pillars; messaging |
| `fidget-enthusiast-value-prop.md` | Enthusiast: durable, fidget anywhere, easy to choose |
| `gift-buyer-value-prop.md` | Gift: right type, premium at budget, delivery, story |
| `collector-value-prop.md` | Collector: drops, worldwide/free ship, universe to collect |

### Use Cases (`use-cases/`)
| File | Description |
|------|-------------|
| `desk-and-pocket-fidget.md` | Premium spinner/slider for focus and stress relief |
| `discreet-fidget-meetings-and-travel.md` | Ring/pendant for meetings and travel |
| `thoughtful-gift.md` | Gift buyer chooses and gives LAUTIE |
| `collecting-limited-editions.md` | Collector tracks drops and co-brands |

### Competitors (`competitors/`)
| File | Description |
|------|-------------|
| `generic-and-amazon-fidgets.md` | Mass-market, cheap; when we win/lose; battlecard |
| `other-premium-edc-brands.md` | Other premium metal fidget/EDC; differentiators; add named later |

### Objections (`objections/`)
| File | Description |
|------|-------------|
| `common-objections.md` | All personas: price, competition, need, gift, collector |
| `fidget-enthusiast-objections.md` | Enthusiast objection handling |
| `gift-buyer-objections.md` | Gift buyer objection handling |
| `collector-objections.md` | Collector objection handling |

### Case Studies (`case-studies/`)
| File | Description |
|------|-------------|
| `enthusiast-upgrade-story.md` | Composite: upgrade from cheap; slider + ring |
| `gift-buyer-story.md` | Composite: thoughtful gift; pendant + pouch |

### Sales Plays (`sales-plays/`)
| File | Description |
|------|-------------|
| `enthusiast-upgrade-from-cheap.md` | Convert visitors ready to upgrade; lifecycle add ring/pendant |
| `gift-occasion-play.md` | Gift buyers; seasonal and occasion; simplify choice and delivery |
| `collector-drop-and-restock.md` | Drops and restocks; newsletter and News; reduce miss rate |

---

## Loading Rules for AI Agents

1. **Quick context**: Load `README.md` first for company, products, personas, competitors, objections, and plays.
2. **Deep dive**: Use this INDEX to load specific files (e.g. persona + pain points + value prop for a given segment).
3. **Topic → file**: Use the tables above to map topic (e.g. “gift,” “collector,” “objection,” “competitor”) to the right file.
4. **Scraping**: `scraping.log` and optional `homepage.json` in this company directory for scrape history and raw data.

---

## Related Commands

- `/continue lautie` — Continue workflow from current phase
- `/add product lautie` — Add a product
- `/add persona lautie` — Add a persona
- `/add competitor lautie` — Add a competitor
- `/status lautie` — Show progress
- `/generate-index lautie` — Regenerate this INDEX
- `/generate-readme lautie` — Regenerate README.md

---
*Last updated: 2026-02-03*
*Generated by Sales Brain*

## V1 Loading Note

- Prefer files with complete `Evidence & Sources` entries.
- Treat `To be verified` claims as hypotheses, not final proof.
