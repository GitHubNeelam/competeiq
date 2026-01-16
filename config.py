"""Configuration"""

import os

# API Keys
TINYFISH_API_KEY = 'sk-mino-VCLM3j49kBiW3hhKzlG1tWW-dYSB_yhI'
YUTORI_API_KEY = 'yt_0N8-AA8miCQgFquxcg_PljwZXulVkeTbmgjsM3pePAk'

# API Endpoints
TINYFISH_API_URL = "https://mino.ai/v1/automation/run-sse"
YUTORI_API_URL = "https://api.yutori.ai/v1/chat/completions"

# Competitors
COMPETITORS = {
    'notion': {
        'name': 'Notion',
        'pricing_url': 'https://www.notion.so/pricing',
        'features_url': 'https://www.notion.so/product',
    },
    'clickup': {
        'name': 'ClickUp',
        'pricing_url': 'https://clickup.com/pricing',
        'features_url': 'https://clickup.com/features',
    },
    'monday': {
        'name': 'Monday.com',
        'pricing_url': 'https://monday.com/pricing',
        'features_url': 'https://monday.com/product',
    }
}

# File paths
DATA_DIR = 'data'
RAW_DATA_FILE = f'{DATA_DIR}/raw_data.json'
INSIGHTS_FILE = f'{DATA_DIR}/insights.json'
