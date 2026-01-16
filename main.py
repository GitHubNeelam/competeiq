"""CompeteIQ - Main Orchestrator"""

import json
from scraper import CompetitorScraper
from analyzer import CompetitiveAnalyzer
from mock_data import MOCK_RAW_DATA, MOCK_INSIGHTS
from config import *
import os

def run_intelligence_pipeline(use_mock=False):
    """Run the complete pipeline"""
    print("\n" + "="*60)
    print("🚀 COMPETEIQ - COMPETITIVE INTELLIGENCE AGENT")
    print("="*60)
    
    if use_mock:
        print("\n⚠️  USING MOCK DATA")
        
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(RAW_DATA_FILE, 'w') as f:
            json.dump(MOCK_RAW_DATA, f, indent=2)
        with open(INSIGHTS_FILE, 'w') as f:
            json.dump(MOCK_INSIGHTS, f, indent=2)
        
        print(f"✅ Mock data saved!")
        return MOCK_INSIGHTS
    
    # Real APIs
    print("\n📍 STEP 1: Scraping...")
    scraper = CompetitorScraper()
    raw_data = scraper.scrape_all_competitors()
    
    print("\n📍 STEP 2: AI Analysis...")
    analyzer = CompetitiveAnalyzer()
    insights = analyzer.analyze_all()
    
    print("\n✅ PIPELINE COMPLETE!")
    return insights


def display_summary(insights_file=INSIGHTS_FILE):
    """Display summary"""
    if not os.path.exists(insights_file):
        print(f"❌ No insights found")
        return
    
    with open(insights_file, 'r') as f:
        insights = json.load(f)
    
    print("\n" + "="*60)
    print("📊 COMPETITIVE INTELLIGENCE SUMMARY")
    print("="*60)
    
    for comp_id, comp_data in insights['competitors'].items():
        print(f"\n🏢 {comp_data['name']}")
        analysis = comp_data.get('analysis', {})
        
        if 'pricing' in analysis:
            print(f"   💰 Starting: {analysis['pricing'].get('starting_price', 'N/A')}")
        if 'target_market' in analysis:
            print(f"   🎯 {analysis['target_market']}")
        if 'key_features' in analysis:
            features = ', '.join(analysis['key_features'][:3])
            print(f"   ⭐ {features}...")
    
    if insights.get('comparison'):
        comp = insights['comparison']
        if 'strategic_recommendations' in comp:
            print("\n💡 TOP RECOMMENDATIONS:")
            for i, rec in enumerate(comp['strategic_recommendations'][:3], 1):
                print(f"   {i}. {rec}")
    
    print("\n" + "="*60)
    print(f"📁 Data saved: {INSIGHTS_FILE}")
    print("="*60)


if __name__ == "__main__":
    # START WITH MOCK DATA
    # Change to False when ready for real APIs
    insights = run_intelligence_pipeline(use_mock=True)
    
    if insights:
        display_summary()
