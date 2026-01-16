"""Configuration"""

import os

# API Keys
TINYFISH_API_KEY = 'sk-mino-VCLM3j49kBiW3hhKzlG1tWW-dYSB_yhI'
YUTORI_API_KEY = 'yt_0N8-AA8miCQgFquxcg_PljwZXulVkeTbmgjsM3pePAk'

# API Endpoints
TINYFISH_API_URL = "https://mino.ai/v1/automation/run-sse"
YUTORI_API_URL = "https://api.yutori.ai/v1/chat/completions"

# Competitors - Now with 6 pages each for deep analysis
COMPETITORS = {
    'notion': {
        'name': 'Notion',
        'homepage_url': 'https://www.notion.so',
        'pricing_url': 'https://www.notion.so/pricing',
        'features_url': 'https://www.notion.so/product',
        'g2_url': 'https://www.g2.com/products/notion/reviews',
        'changelog_url': 'https://www.notion.so/releases',
        'customers_url': 'https://www.notion.so/customers',
    },
    'airtable': {
        'name': 'Airtable',
        'homepage_url': 'https://www.airtable.com',
        'pricing_url': 'https://www.airtable.com/pricing',
        'features_url': 'https://www.airtable.com/platform',
        'g2_url': 'https://www.g2.com/products/airtable/reviews',
        'changelog_url': 'https://www.airtable.com/newsroom',
        'customers_url': 'https://www.airtable.com/customers',
    },
    'clickup': {
        'name': 'ClickUp',
        'homepage_url': 'https://clickup.com',
        'pricing_url': 'https://clickup.com/pricing',
        'features_url': 'https://clickup.com/features',
        'g2_url': 'https://www.g2.com/products/clickup/reviews',
        'changelog_url': 'https://clickup.com/release-notes',
        'customers_url': 'https://clickup.com/customers',
    }
}
# File paths
DATA_DIR = 'data'
RAW_DATA_FILE = f'{DATA_DIR}/raw_data.json'
INSIGHTS_FILE = f'{DATA_DIR}/insights.json'

