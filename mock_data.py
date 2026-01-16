"""Mock data for testing"""

from datetime import datetime

MOCK_RAW_DATA = {
    'scraped_at': datetime.now().isoformat(),
    'competitors': {
        'notion': {
            'name': 'Notion',
            'pages': {
                'pricing': {'content': 'Free: $0, Plus: $8/user/mo, Business: $15/user/mo', 'status': 'success'},
                'features': {'content': 'Wikis, Projects, Docs, AI assistant', 'status': 'success'}
            }
        },
        'clickup': {
            'name': 'ClickUp',
            'pages': {
                'pricing': {'content': 'Free: $0, Unlimited: $7/user/mo, Business: $12/user/mo', 'status': 'success'},
                'features': {'content': 'Tasks, Docs, Goals, Time tracking', 'status': 'success'}
            }
        },
        'monday': {
            'name': 'Monday.com',
            'pages': {
                'pricing': {'content': 'Basic: $9/user/mo, Standard: $12/user/mo', 'status': 'success'},
                'features': {'content': 'Boards, Automations, Integrations', 'status': 'success'}
            }
        }
    }
}

MOCK_INSIGHTS = {
    'analyzed_at': datetime.now().isoformat(),
    'competitors': {
        'notion': {
            'name': 'Notion',
            'analysis': {
                'pricing': {'tiers': ['Free: $0', 'Plus: $8/mo', 'Business: $15/mo'], 'starting_price': '$0'},
                'key_features': ['Wikis', 'Projects', 'Docs', 'AI assistant'],
                'target_market': 'SMB to Mid-market',
                'competitive_advantages': ['Lower pricing', 'Strong brand'],
                'potential_gaps': ['Limited automation']
            }
        },
        'clickup': {
            'name': 'ClickUp',
            'analysis': {
                'pricing': {'tiers': ['Free: $0', 'Unlimited: $7/mo'], 'starting_price': '$0'},
                'key_features': ['Tasks', 'Time tracking', 'Goals'],
                'target_market': 'Power users',
                'competitive_advantages': ['Feature-rich', 'Customizable'],
                'potential_gaps': ['Complex interface']
            }
        },
        'monday': {
            'name': 'Monday.com',
            'analysis': {
                'pricing': {'tiers': ['Basic: $9/mo', 'Standard: $12/mo'], 'starting_price': '$9'},
                'key_features': ['Visual boards', 'Automations'],
                'target_market': 'Visual teams',
                'competitive_advantages': ['Great UX', 'Easy to use'],
                'potential_gaps': ['Higher price']
            }
        }
    },
    'comparison': {
        'market_overview': 'Competitive productivity market with $7-15/mo pricing',
        'strategic_recommendations': [
            'Price at $10/mo between ClickUp and Monday',
            'Combine Notion simplicity with ClickUp features',
            'Target mid-market teams'
        ]
    }
}
