"""AI analyzer using Yutori API"""

import requests
import json
from datetime import datetime
from config import *
import os

class CompetitiveAnalyzer:
    def __init__(self):
        self.api_key = YUTORI_API_KEY
        self.api_url = YUTORI_API_URL
        
    def call_yutori(self, prompt):
        """Call Yutori API"""
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'model': 'gpt-4o-mini',
                'messages': [
                    {'role': 'system', 'content': 'You are a competitive analyst. Return only valid JSON.'},
                    {'role': 'user', 'content': prompt}
                ],
                'temperature': 0.3,
                'max_tokens': 2000
            }
            
            print(f"    🤖 Calling Yutori AI...")
            
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=60
            )
            
            if response.status_code == 200:
                content = response.json()['choices'][0]['message']['content']
                print(f"    ✅ Got response")
                return content
            else:
                print(f"    ❌ Failed: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"    ❌ Error: {str(e)}")
            return None
    
    def analyze_competitor(self, comp_data):
        """Analyze one competitor with deep intelligence"""
        print(f"\n🧠 Analyzing {comp_data['name']}...")
        
        # Gather all page content
        homepage = comp_data['pages'].get('homepage', {}).get('content', '')[:2000]
        pricing = comp_data['pages'].get('pricing', {}).get('content', '')[:2000]
        features = comp_data['pages'].get('features', {}).get('content', '')[:2000]
        g2_reviews = comp_data['pages'].get('g2', {}).get('content', '')[:2000]
        changelog = comp_data['pages'].get('changelog', {}).get('content', '')[:2000]
        customers = comp_data['pages'].get('customers', {}).get('content', '')[:2000]
        
        if not any([homepage, pricing, features]):
            print(f"    ⚠️ Insufficient data to analyze")
            return None
        
        prompt = f"""
Analyze this competitor deeply and return ONLY valid JSON:

COMPETITOR: {comp_data['name']}

HOMEPAGE (Value Proposition):
{homepage}

PRICING:
{pricing}

FEATURES:
{features}

G2 REVIEWS:
{g2_reviews}

RECENT LAUNCHES (Changelog):
{changelog}

CUSTOMERS:
{customers}

Extract comprehensive intelligence and return in this EXACT JSON format:
{{
  "core_value_prop": "One sentence positioning from homepage",
  "pricing": {{
    "tiers": ["List all tiers with prices"],
    "starting_price": "Lowest paid price",
    "has_free_tier": true/false,
    "enterprise_pricing": "Custom/Contact/Specific"
  }},
  "key_features": ["Top 7-10 features"],
  "customer_sentiment": {{
    "rating": "X.X/5 if found, or 'Unknown'",
    "review_count": "Number or 'Unknown'",
    "top_loved": ["3 things customers love most"],
    "top_frustrations": ["3 main customer complaints"],
    "switching_patterns": "Common alternatives mentioned"
  }},
  "recent_launches": ["Last 3-5 major features or updates"],
  "strategic_focus": "What they're emphasizing (AI, enterprise, automation, etc)",
  "target_signals": {{
    "customer_types": ["Types of companies using it"],
    "size_focus": "Startup/SMB/Mid-market/Enterprise"
  }},
  "growth_motion": "PLG-first/Sales-led/Hybrid (infer from free tier + contact sales prominence)",
  "target_market": "Primary customer segment",
  "competitive_advantages": ["5 key strengths"],
  "potential_gaps": ["5 weaknesses or missing capabilities"],
  "strategic_vulnerabilities": ["3 risks or threats to their position"]
}}

Be specific and factual. Extract actual data, don't make assumptions.
"""
        
        result = self.call_yutori(prompt)
        
        if result:
            try:
                # Clean markdown formatting
                if '```json' in result:
                    result = result.split('```json')[1].split('```')[0].strip()
                elif '```' in result:
                    result = result.split('```')[1].split('```')[0].strip()
                
                parsed = json.loads(result)
                print(f"    ✅ Extracted {len(parsed)} data points")
                return parsed
            except Exception as e:
                print(f"    ⚠️ JSON parse error: {str(e)}")
                return {'raw': result}
        
        return None
    
    def generate_comparison(self, all_analyses):
        """Generate comparison"""
        print("\n📊 Generating comparison...")
        
        prompt = f"""
Compare these competitors and return ONLY valid JSON:

{json.dumps(all_analyses, indent=2)}

Return format:
{{
  "market_overview": "2-3 sentence summary of competitive landscape",
  "pricing_comparison": {{
    "range": "price range across all competitors",
    "positioning": "who's budget/mid/premium"
  }},
  "feature_gaps": ["key features some have that others lack"],
  "market_opportunities": ["underserved segments or gaps"],
  "strategic_recommendations": [
    "5-7 specific, actionable recommendations"
  ],
  "threats": ["competitive threats to watch"],
  "advantages": ["opportunities to leverage"]
}}
"""
        
        result = self.call_yutori(prompt)
        
        if result:
            try:
                if '```json' in result:
                    result = result.split('```json')[1].split('```')[0].strip()
                elif '```' in result:
                    result = result.split('```')[1].split('```')[0].strip()
                return json.loads(result)
            except:
                return {'raw': result}
        
        return None
    
    def analyze_all(self):
        """Analyze all data"""
        print("\n" + "="*60)
        print("🧠 STARTING AI ANALYSIS")
        print("="*60)
        
        if not os.path.exists(RAW_DATA_FILE):
            print(f"❌ No data found")
            return None
        
        with open(RAW_DATA_FILE, 'r') as f:
            raw_data = json.load(f)
        
        insights = {
            'analyzed_at': datetime.now().isoformat(),
            'competitors': {},
            'comparison': None
        }
        
        for comp_id, comp_data in raw_data['competitors'].items():
            analysis = self.analyze_competitor(comp_data)
            if analysis:
                insights['competitors'][comp_id] = {
                    'name': comp_data['name'],
                    'analysis': analysis
                }
        
        if insights['competitors']:
            insights['comparison'] = self.generate_comparison(insights['competitors'])
        
        with open(INSIGHTS_FILE, 'w') as f:
            json.dump(insights, f, indent=2)
        
        print(f"\n✅ Analysis complete! Saved to {INSIGHTS_FILE}")
        return insights


if __name__ == "__main__":
    analyzer = CompetitiveAnalyzer()
    analyzer.analyze_all()
