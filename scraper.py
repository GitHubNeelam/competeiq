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
        
    def scrape_url(self, url):
        """Scrape a single URL"""
        print(f"  🕷️  Scraping: {url}")
        
        if 'pricing' in url:
            goal = f"Extract all pricing tiers and prices from {url}. Return as text."
        else:
            goal = f"Extract all key features from {url}. Return as text."
        
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
                timeout=60,
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
                            except:
                                pass
                
                print(f"    ✅ Success! Got {len(content)} characters")
                return {
                    'url': url,
                    'content': content,
                    'status': 'success',
                    'scraped_at': datetime.now().isoformat()
                }
            else:
                print(f"    ❌ Failed: {response.status_code}")
                return {'url': url, 'content': '', 'status': 'failed'}
                
        except Exception as e:
            print(f"    ❌ Error: {str(e)}")
            return {'url': url, 'content': '', 'status': 'error', 'error': str(e)}
    
    def scrape_competitor(self, comp_id, comp_info):
        """Scrape one competitor"""
        print(f"\n📊 Scraping {comp_info['name']}...")
        
        results = {
            'name': comp_info['name'],
            'pages': {}
        }
        
        if 'pricing_url' in comp_info:
            results['pages']['pricing'] = self.scrape_url(comp_info['pricing_url'])
            time.sleep(2)
        
        if 'features_url' in comp_info:
            results['pages']['features'] = self.scrape_url(comp_info['features_url'])
            time.sleep(2)
        
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
