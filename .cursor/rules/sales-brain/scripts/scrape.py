#!/usr/bin/env python3
"""
Sales Brain - Company and Product Research Assistant
A tool for gathering and organizing sales intelligence about companies and their products.
"""

import os
import re
import json
import argparse
from pathlib import Path
from urllib.parse import urlparse, urljoin
from datetime import datetime

try:
    import requests
    from bs4 import BeautifulSoup
    SCRAPING_AVAILABLE = True
except ImportError:
    SCRAPING_AVAILABLE = False
    print("Note: Install 'requests' and 'beautifulsoup4' for web scraping capabilities")


class SalesBrain:
    """Main class for the Sales Brain research assistant."""
    
    def __init__(self, output_dir: str = "."):
        self.output_dir = Path(output_dir)
        self.products_dir = self.output_dir / "products"
        self.company_file = self.output_dir / "company.md"
        self.company_data = {}
        self.products = []
        self.pages_scraped = 0
        
    def ensure_directories(self):
        """Create necessary directories if they don't exist."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.products_dir.mkdir(parents=True, exist_ok=True)
        
    def scrape_website(self, url: str) -> dict:
        """Scrape a website for company information."""
        if not SCRAPING_AVAILABLE:
            return {"error": "Scraping libraries not installed. Run: pip install requests beautifulsoup4"}
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract basic information
            data = {
                "url": url,
                "title": self._get_title(soup),
                "description": self._get_meta_description(soup),
                "headings": self._get_headings(soup),
                "links": self._get_important_links(soup, url),
                "text_content": self._get_main_text(soup),
                "scraped_at": datetime.now().isoformat()
            }
            
            self.pages_scraped += 1
            self._update_scraping_log(url)
            return data
            
        except requests.RequestException as e:
            return {"error": str(e), "url": url}
    
    def scrape_with_follow(self, url: str, follow: str = None, max_pages: int = 10) -> dict:
        """Scrape a URL and optionally follow discovered links.
        
        Args:
            url: The starting URL to scrape
            follow: Category of links to follow: 'about', 'products', 'pricing', 'contact', 'all', or None
            max_pages: Maximum number of pages to scrape (default 10)
        
        Returns:
            Dict with 'main' page data and 'followed' list of additional pages
        """
        # Parse base domain to avoid following external links
        parsed_base = urlparse(url)
        base_domain = parsed_base.netloc
        
        # Scrape the main page
        print(f"🔍 Scraping: {url}", file=__import__('sys').stderr)
        main_data = self.scrape_website(url)
        
        result = {
            "main": main_data,
            "followed": [],
            "total_pages": 1
        }
        
        if "error" in main_data or not follow:
            return result
        
        # Determine which link categories to follow
        if follow == "all":
            categories = ["about", "products", "pricing", "contact"]
        else:
            categories = [cat.strip() for cat in follow.split(",")]
        
        # Collect URLs to follow
        urls_to_follow = []
        scraped_urls = {url}  # Track already scraped URLs
        
        for category in categories:
            if category in main_data.get("links", {}):
                for link in main_data["links"][category]:
                    link_url = link.get("url", "")
                    # Only follow links on the same domain
                    parsed_link = urlparse(link_url)
                    if parsed_link.netloc == base_domain and link_url not in scraped_urls:
                        urls_to_follow.append({
                            "url": link_url,
                            "category": category,
                            "text": link.get("text", "")
                        })
                        scraped_urls.add(link_url)
        
        # Scrape followed URLs (up to max_pages - 1, since we already scraped main)
        for link_info in urls_to_follow[:max_pages - 1]:
            link_url = link_info["url"]
            print(f"🔍 Following [{link_info['category']}]: {link_url}", file=__import__('sys').stderr)
            
            followed_data = self.scrape_website(link_url)
            followed_data["_category"] = link_info["category"]
            followed_data["_link_text"] = link_info["text"]
            result["followed"].append(followed_data)
            result["total_pages"] += 1
        
        return result
    
    def _update_scraping_log(self, url: str):
        """Log the scraped URL to scraping.log."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = self.output_dir / "scraping.log"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {url}\n")
    
    def _get_title(self, soup: BeautifulSoup) -> str:
        """Extract page title."""
        title = soup.find('title')
        return title.get_text().strip() if title else ""
    
    def _get_meta_description(self, soup: BeautifulSoup) -> str:
        """Extract meta description."""
        meta = soup.find('meta', attrs={'name': 'description'})
        if meta:
            return meta.get('content', '')
        
        # Try Open Graph description
        og_desc = soup.find('meta', attrs={'property': 'og:description'})
        if og_desc:
            return og_desc.get('content', '')
        
        return ""
    
    def _get_headings(self, soup: BeautifulSoup) -> list:
        """Extract all headings."""
        headings = []
        for tag in ['h1', 'h2', 'h3']:
            for heading in soup.find_all(tag):
                text = heading.get_text().strip()
                if text:
                    headings.append({"level": tag, "text": text})
        return headings[:20]  # Limit to first 20
    
    def _get_important_links(self, soup: BeautifulSoup, base_url: str) -> dict:
        """Extract important navigation links."""
        links = {
            "about": [],
            "products": [],
            "pricing": [],
            "contact": [],
            "other": []
        }
        
        keywords = {
            "about": ["about", "company", "team", "story", "mission"],
            "products": ["product", "solution", "service", "feature", "platform"],
            "pricing": ["pricing", "price", "plan", "cost"],
            "contact": ["contact", "support", "help"]
        }
        
        for a in soup.find_all('a', href=True):
            href = a.get('href', '')
            text = a.get_text().strip().lower()
            
            if not href or href.startswith('#') or href.startswith('javascript:'):
                continue
                
            full_url = urljoin(base_url, href)
            
            categorized = False
            for category, kws in keywords.items():
                if any(kw in text or kw in href.lower() for kw in kws):
                    if full_url not in [l['url'] for l in links[category]]:
                        links[category].append({
                            "text": a.get_text().strip(),
                            "url": full_url
                        })
                    categorized = True
                    break
        
        # Limit results
        for category in links:
            links[category] = links[category][:5]
            
        return links
    
    def _get_main_text(self, soup: BeautifulSoup) -> str:
        """Extract main text content."""
        # Remove script and style elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        text = soup.get_text(separator=' ', strip=True)
        # Clean up whitespace
        text = re.sub(r'\s+', ' ', text)
        return text[:5000]  # Limit to first 5000 chars
    
    def generate_company_md(self, company_name: str, url: str, scraped_data: dict = None) -> str:
        """Generate company.md content."""
        template = f"""# {company_name}

## Overview
{scraped_data.get('description', '[To be filled based on research]') if scraped_data else '[To be filled based on research]'}

## Industry
[To be determined]

## Founded
[Unknown]

## Headquarters
[Unknown]

## Company Size
[Unknown]

## Mission/Vision
[To be determined from research]

## Target Market
[To be determined]

## Key Differentiators
[To be determined]

## Website
{url}

## Scraped Information

### Page Title
{scraped_data.get('title', 'N/A') if scraped_data else 'N/A'}

### Key Headings Found
{self._format_headings(scraped_data.get('headings', [])) if scraped_data else 'N/A'}

### Important Links Discovered
{self._format_links(scraped_data.get('links', {})) if scraped_data else 'N/A'}

## Additional Notes
- Research date: {datetime.now().strftime('%Y-%m-%d')}
- Status: Pending review

---
*Generated by Sales Brain*
"""
        return template
    
    def _format_headings(self, headings: list) -> str:
        """Format headings for markdown."""
        if not headings:
            return "None found"
        return "\n".join([f"- [{h['level'].upper()}] {h['text']}" for h in headings])
    
    def _format_links(self, links: dict) -> str:
        """Format links for markdown."""
        output = []
        for category, items in links.items():
            if items:
                output.append(f"\n**{category.title()}:**")
                for link in items:
                    output.append(f"- [{link['text']}]({link['url']})")
        return "\n".join(output) if output else "None found"
    
    def generate_product_md(self, product_name: str, company_name: str, 
                           features: list = None, problem: str = None,
                           value_prop: str = None, competition: list = None) -> str:
        """Generate product markdown content."""
        features_md = "\n".join([f"- {f}" for f in (features or ["[To be determined]"])])
        
        competition_md = "| Competitor | Key Difference |\n|------------|----------------|\n"
        if competition:
            for comp in competition:
                competition_md += f"| {comp.get('name', 'Unknown')} | {comp.get('difference', 'TBD')} |\n"
        else:
            competition_md += "| [To be researched] | [To be determined] |\n"
        
        template = f"""# {product_name}

## Company
{company_name}

## Overview
[Product description to be researched]

## Main Features
{features_md}

## Problem Solved
{problem or '[What customer problem does this solve?]'}

## Value Proposition
{value_prop or '[What unique value does this product provide?]'}

## Target Customers
[Ideal customer profile to be determined]

## Competition
{competition_md}

## Pricing Model
[To be researched if publicly available]

## Additional Notes
- Research date: {datetime.now().strftime('%Y-%m-%d')}
- Status: Pending review

---
*Generated by Sales Brain*
"""
        return template
    
    def save_company(self, content: str):
        """Save company.md file."""
        self.ensure_directories()
        self.company_file.write_text(content, encoding='utf-8')
        print(f"✅ Saved: {self.company_file}")
    
    def save_product(self, product_name: str, content: str):
        """Save product markdown file."""
        self.ensure_directories()
        # Create slug from product name
        slug = re.sub(r'[^a-z0-9]+', '-', product_name.lower()).strip('-')
        product_file = self.products_dir / f"{slug}.md"
        product_file.write_text(content, encoding='utf-8')
        print(f"✅ Saved: {product_file}")
        return product_file
    
    def load_company(self) -> str:
        """Load existing company.md if it exists."""
        if self.company_file.exists():
            return self.company_file.read_text(encoding='utf-8')
        return None
    
    def list_products(self) -> list:
        """List all product files."""
        if not self.products_dir.exists():
            return []
        return list(self.products_dir.glob("*.md"))
    
    def interactive_start(self):
        """Start interactive mode."""
        print("\n" + "="*50)
        print("🧠 SALES BRAIN - Company Research Assistant")
        print("="*50 + "\n")
        
        # Get company info
        company_name = input("Enter company name: ").strip()
        if not company_name:
            print("❌ Company name is required")
            return
            
        website_url = input("Enter website URL: ").strip()
        if not website_url:
            print("❌ Website URL is required")
            return
            
        # Ensure URL has protocol
        if not website_url.startswith(('http://', 'https://')):
            website_url = 'https://' + website_url
        
        print(f"\n🔍 Researching {company_name}...")
        
        # Scrape website
        scraped_data = self.scrape_website(website_url)
        
        if "error" in scraped_data:
            print(f"⚠️ Scraping warning: {scraped_data['error']}")
            scraped_data = None
        
        # Generate and save company.md
        company_content = self.generate_company_md(company_name, website_url, scraped_data)
        self.save_company(company_content)
        
        # Show to user
        print("\n" + "-"*50)
        print("📄 COMPANY INFORMATION")
        print("-"*50)
        print(company_content[:2000] + "..." if len(company_content) > 2000 else company_content)
        
        # Confirmation loop
        while True:
            response = input("\n✅ Does this look accurate? (yes/no): ").strip().lower()
            
            if response in ['yes', 'y']:
                print("\n✅ Company information confirmed!")
                break
            elif response in ['no', 'n']:
                changes = input("What should be changed? (describe the changes): ").strip()
                print(f"\n📝 Note: Please manually edit company.md with these changes: {changes}")
                print(f"   File location: {self.company_file.absolute()}")
                input("Press Enter after making changes...")
                
                # Reload and show again
                updated_content = self.load_company()
                if updated_content:
                    print("\n" + "-"*50)
                    print("📄 UPDATED COMPANY INFORMATION")
                    print("-"*50)
                    print(updated_content[:2000] + "..." if len(updated_content) > 2000 else updated_content)
            else:
                print("Please enter 'yes' or 'no'")
        
        # Product detection
        print("\n🔍 Detecting products...")
        self._detect_products(company_name, scraped_data)
    
    def _detect_products(self, company_name: str, scraped_data: dict = None):
        """Detect and create product files."""
        # Check if we have product links
        product_links = []
        if scraped_data and 'links' in scraped_data:
            product_links = scraped_data['links'].get('products', [])
        
        if product_links:
            print(f"\n📦 Found {len(product_links)} potential product pages:")
            for i, link in enumerate(product_links, 1):
                print(f"   {i}. {link['text']} - {link['url']}")
        
        # Ask user to identify products
        print("\n📝 Let's identify the products.")
        print("Enter product names one at a time (or 'done' to finish):\n")
        
        products = []
        while True:
            product_name = input("Product name (or 'done'): ").strip()
            
            if product_name.lower() == 'done':
                break
            
            if product_name:
                products.append(product_name)
                print(f"   ✅ Added: {product_name}")
        
        if not products:
            print("\n⚠️ No products added. You can add them later with /add product")
            return
        
        # Create product files
        print(f"\n📁 Creating {len(products)} product files...")
        
        for product_name in products:
            content = self.generate_product_md(product_name, company_name)
            product_file = self.save_product(product_name, content)
        
        print(f"\n✅ Created {len(products)} product files in {self.products_dir}")
        print("\n📋 Product Summary:")
        for pf in self.list_products():
            print(f"   - {pf.name}")
        
        print("\n🎉 Sales Brain setup complete!")
        print(f"   Company file: {self.company_file}")
        print(f"   Products dir: {self.products_dir}")
        print(f"\n📊 Total pages scraped: {self.pages_scraped}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Sales Brain - Company and Product Research Assistant"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Start command
    start_parser = subparsers.add_parser('start', help='Start interactive research')
    start_parser.add_argument('--output', '-o', default='.', help='Output directory')
    
    # Scrape command
    scrape_parser = subparsers.add_parser('scrape', help='Scrape a URL')
    scrape_parser.add_argument('url', help='URL to scrape')
    scrape_parser.add_argument('--output', '-o', help='Output JSON file')
    scrape_parser.add_argument('--log-dir', '-d', default='.', help='Directory for scraping.log (default: current directory)')
    scrape_parser.add_argument('--follow', '-f', 
                               help='Follow discovered links: about, products, pricing, contact, all (comma-separated)')
    scrape_parser.add_argument('--max-pages', '-m', type=int, default=10,
                               help='Maximum pages to scrape when following links (default: 10)')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List products')
    list_parser.add_argument('--dir', '-d', default='.', help='Directory to search')
    
    args = parser.parse_args()
    
    if args.command == 'start':
        brain = SalesBrain(args.output)
        brain.interactive_start()
        
    elif args.command == 'scrape':
        brain = SalesBrain(args.log_dir)
        
        if args.follow:
            # Use follow mode to scrape multiple pages
            data = brain.scrape_with_follow(args.url, follow=args.follow, max_pages=args.max_pages)
        else:
            # Single page scrape
            data = brain.scrape_website(args.url)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            print(f"✅ Saved to {args.output}", file=__import__('sys').stderr)
        else:
            print(json.dumps(data, indent=2))
        
        print(f"\n📊 Total pages scraped: {brain.pages_scraped}", file=__import__('sys').stderr)
            
    elif args.command == 'list':
        brain = SalesBrain(args.dir)
        products = brain.list_products()
        
        if products:
            print(f"📦 Found {len(products)} products:")
            for p in products:
                print(f"   - {p.name}")
        else:
            print("No products found")
            
    else:
        # Default: start interactive mode
        brain = SalesBrain()
        brain.interactive_start()


if __name__ == "__main__":
    main()
