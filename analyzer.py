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
