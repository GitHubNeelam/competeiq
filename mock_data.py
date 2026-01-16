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
                'features': {'content': 'Tasks,
