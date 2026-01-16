"""Web scraper using TinyFish API"""

import requests
import json
from datetime import datetime
from config import *
import os
import time

class CompetitorScraper:
    def __init__(self):
        self.api_key = TINYFISH_API_KEY
        self.api_url = TINYFISH_API_URL
        
    def scrape_url(self, url, page_type='general'):
        """Scrape a single URL with context-aware goals"""
        print(f"  🕷️  Scraping {page_type}: {url}")
        
        # Create smart goals based on page type
        if page_type == 'homepage':
            goal = f"Extract the main value proposition, hero headline, and primary messaging from {url}. Return as detailed text."
        elif page_type == 'pricing':
            goal = f"Extract all pricing tiers, prices, plan names, and whether there's a free tier from {url}. Return as detailed text."
        elif page_type == 'features':
            goal = f"Extract all key features, capabilities, and strategic focus areas from {url}. Return as detailed text."
        elif page_type == 'g2':
            goal = f"Extract the overall rating (out of 5), total number of reviews, common praise themes, and common complaints from {url}. Return as detailed text."
        elif page_type == 'changelog':
            goal = f"Extract recent product launches and new features announced in the last 6 months from {url}. Return as detailed text."
        elif page_type == 'customers':
            goal = f"Extract customer company names, their sizes/industries, and any case study details from {url}. Return as detailed text."
        else:
            goal = f"Extract main content from {url}. Return as detailed text."
        
        try:
            headers = {
                'X-API-Key': self.api_key,
                'Content-Type': 'application/json'
            }
            
            payload = {'url': url, 'goal': goal}
            
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=90,
                stream=True
            )
            
            if response.status_code == 200:
                content = ""
                for line in response.iter_lines():
                    if line:
                        decoded = line.decode('utf-8')
                        if decoded.startswith('data: '):
                            try:
                                data = json.loads(decoded[6:])
                                if 'content' in data:
                                    content += data['content']
                                elif 'result' in data:
                                    content += str(data['result'])
                            except:
                                pass
                
                print(f"    ✅ Success! Got {len(content)} characters")
                return {
                    'url': url,
                    'page_type': page_type,
                    'content': content,
                    'status': 'success',
                    'scraped_at': datetime.now().isoformat()
                }
            else:
                print(f"    ❌ Failed: {response.status_code}")
                return {'url': url, 'page_type': page_type, 'content': '', 'status': 'failed'}
                
        except Exception as e:
            print(f"    ❌ Error: {str(e)}")
            return {'url': url, 'page_type': page_type, 'content': '', 'status': 'error', 'error': str(e)}
    
    def scrape_competitor(self, comp_id, comp_info):
        """Scrape all pages for one competitor"""
        print(f"\n📊 Scraping {comp_info['name']}...")
        
        results = {
            'name': comp_info['name'],
            'pages': {}
        }
        
        # Scrape all 6 page types
        page_types = [
            ('homepage_url', 'homepage'),
            ('pricing_url', 'pricing'),
            ('features_url', 'features'),
            ('g2_url', 'g2'),
            ('changelog_url', 'changelog'),
            ('customers_url', 'customers')
        ]
        
        for url_key, page_type in page_types:
            if url_key in comp_info:
                results['pages'][page_type] = self.scrape_url(
                    comp_info[url_key], 
                    page_type=page_type
                )
                time.sleep(3)  # Be nice to APIs
        
        return results
    
    def scrape_all_competitors(self):
        """Scrape all competitors"""
        print("\n" + "="*60)
        print("🚀 STARTING SCRAPING")
        print("="*60)
        
        all_data = {
            'scraped_at': datetime.now().isoformat(),
            'competitors': {}
        }
        
        for comp_id, comp_info in COMPETITORS.items():
            try:
                all_data['competitors'][comp_id] = self.scrape_competitor(comp_id, comp_info)
            except Exception as e:
                print(f"  ⚠️ Failed: {str(e)}")
        
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(RAW_DATA_FILE, 'w') as f:
            json.dump(all_data, f, indent=2)
        
        print(f"\n✅ Complete! Saved to {RAW_DATA_FILE}")
        return all_data


if __name__ == "__main__":
    scraper = CompetitorScraper()
    scraper.scrape_all_competitors()
