"""Mock data for testing - Enhanced version"""

from datetime import datetime

MOCK_RAW_DATA = {
    'scraped_at': datetime.now().isoformat(),
    'competitors': {
        'notion': {
            'name': 'Notion',
            'pages': {
                'homepage': {'content': 'Write, plan, and get organized. One workspace for you and your team. Notion is the connected workspace where better, faster work happens.', 'status': 'success'},
                'pricing': {'content': 'Free: $0, Plus: $8/user/mo, Business: $15/user/mo, Enterprise: Custom pricing. Free tier includes unlimited pages and blocks.', 'status': 'success'},
                'features': {'content': 'Connected workspace: Docs, Wikis, Projects, Databases, AI assistant, Team collaboration, 100+ integrations, Templates, Real-time collaboration', 'status': 'success'},
                'g2': {'content': 'Rating: 4.7 out of 5 stars. 4,892 reviews. Users love: Flexibility, beautiful UI, all-in-one solution. Common complaints: Performance with large databases, learning curve, limited automation compared to competitors like Airtable.', 'status': 'success'},
                'changelog': {'content': 'Recent launches: Notion AI writing assistant (Nov 2024), Database automations (Sept 2024), Q&A assistant (Aug 2024), Calendar view improvements (July 2024)', 'status': 'success'},
                'customers': {'content': 'Trusted by teams at Figma, Pixar, Nike, Headspace, and thousands of startups. Popular with design teams, engineering teams, and remote-first companies. Company sizes: 10-500 employees primarily.', 'status': 'success'}
            }
        },
        'airtable': {
            'name': 'Airtable',
            'pages': {
                'homepage': {'content': 'Build powerful apps and workflows without code. Airtable is a low-code platform for building next-gen apps. Move beyond rigid tools, operationalize your critical data.', 'status': 'success'},
                'pricing': {'content': 'Free: $0, Team: $20/user/mo, Business: $45/user/mo, Enterprise Scale: Custom. Annual billing saves 20%. Free tier limited to 1,000 records.', 'status': 'success'},
                'features': {'content': 'Connected apps platform: Powerful relational databases, Advanced automations, Interface builder, Extensions marketplace, Views (Grid, Kanban, Calendar, Gallery), Sync, AI fields, Apps, APIs, 1000+ integrations', 'status': 'success'},
                'g2': {'content': 'Rating: 4.6 out of 5 stars. 2,156 reviews. Users love: Powerful databases, automation capabilities, structured data handling, API access. Common complaints: Expensive pricing ($20-45/mo), steep learning curve, overkill for simple use cases. Users often compare with Notion and Smartsheet.', 'status': 'success'},
                'changelog': {'content': 'Recent launches: AI-powered field generation (Oct 2024), Interface designer 2.0 (Sept 2024), Advanced automations (Aug 2024), Enterprise admin controls (July 2024)', 'status': 'success'},
                'customers': {'content': 'Used by teams at Netflix, Expedia, TIME Magazine, Shopify. Popular with operations teams, product teams, and marketing teams. Focus on mid-market to enterprise (50-1000+ employees).', 'status': 'success'}
            }
        },
        'clickup': {
            'name': 'ClickUp',
            'pages': {
                'homepage': {'content': 'One app to replace them all. ClickUp is the everything app for work. Replace all your productivity tools with ClickUp. Docs, Tasks, Goals, Chat, and more.', 'status': 'success'},
                'pricing': {'content': 'Free Forever: $0, Unlimited: $7/user/mo, Business: $12/user/mo, Enterprise: Custom. Free tier includes unlimited tasks and members. One app to replace them all marketing.', 'status': 'success'},
                'features': {'content': 'Everything in one: Tasks, Docs, Goals, Time tracking, Dashboards, Automations, Whiteboards, Chat, Forms, Mind maps, Gantt charts, Calendar, Workload view, Custom fields, 1000+ integrations, Everything view', 'status': 'success'},
                'g2': {'content': 'Rating: 4.7 out of 5 stars. 8,912 reviews. Users love: Feature-rich, highly customizable, best value for money, all-in-one platform. Common complaints: Overwhelming number of features, cluttered interface, steep learning curve, setup takes significant time. Often compared with Asana, Monday, and Notion.', 'status': 'success'},
                'changelog': {'content': 'Recent launches: ClickUp Brain AI (Nov 2024), Universal Search (Oct 2024), Whiteboards 2.0 (Sept 2024), Advanced automations (Aug 2024), Chat view improvements (July 2024)', 'status': 'success'},
                'customers': {'content': 'Used by teams at Google, Airbnb, Uber, Netflix. Popular with agencies, fast-growing startups, and remote teams. Power users and productivity enthusiasts. Company sizes: 10-500 employees.', 'status': 'success'}
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
                'core_value_prop': 'Write, plan, and get organized in one connected workspace',
                'pricing': {
                    'tiers': ['Free: $0', 'Plus: $8/user/mo', 'Business: $15/user/mo', 'Enterprise: Custom'],
                    'starting_price': '$0',
                    'has_free_tier': True,
                    'enterprise_pricing': 'Custom'
                },
                'key_features': ['Connected workspace', 'Docs and wikis', 'Databases', 'AI assistant', 'Team collaboration', '100+ integrations', 'Real-time editing'],
                'customer_sentiment': {
                    'rating': '4.7/5',
                    'review_count': '4,892',
                    'top_loved': ['Flexibility and customization', 'Beautiful and intuitive UI', 'All-in-one solution'],
                    'top_frustrations': ['Performance issues with large databases', 'Learning curve for new users', 'Limited automation vs Airtable'],
                    'switching_patterns': 'Users often move from Google Docs, Evernote. Power users hitting database limits switch to Airtable.'
                },
                'recent_launches': ['Notion AI writing assistant', 'Database automations', 'Q&A assistant', 'Calendar view improvements'],
                'strategic_focus': 'AI integration and enterprise features',
                'target_signals': {
                    'customer_types': ['Design teams', 'Engineering teams', 'Remote-first companies', 'Startups'],
                    'size_focus': 'SMB to Mid-market (10-500 employees)'
                },
                'growth_motion': 'PLG-first with sales assist for enterprise',
                'target_market': 'Knowledge workers and modern teams',
                'competitive_advantages': ['Lowest paid tier pricing', 'Strong brand and community', 'Best for documentation', 'Clean minimal UI', 'Generous free tier'],
                'potential_gaps': ['Database features less powerful than Airtable', 'Limited automation capabilities', 'Performance with heavy data', 'Can overwhelm new users', 'Lacks advanced PM features'],
                'strategic_vulnerabilities': ['Airtable targeting database users', 'Performance issues at scale', 'Increasing competition from Microsoft Loop']
            }
        },
        'airtable': {
            'name': 'Airtable',
            'analysis': {
                'core_value_prop': 'Build powerful apps and workflows without code',
                'pricing': {
                    'tiers': ['Free: $0', 'Team: $20/user/mo', 'Business: $45/user/mo', 'Enterprise: Custom'],
                    'starting_price': '$0',
                    'has_free_tier': True,
                    'enterprise_pricing': 'Custom'
                },
                'key_features': ['Relational databases', 'Advanced automations', 'Interface builder', 'Extensions marketplace', 'Multiple views', 'APIs', 'Enterprise security'],
                'customer_sentiment': {
                    'rating': '4.6/5',
                    'review_count': '2,156',
                    'top_loved': ['Powerful database capabilities', 'Automation features', 'Structured data handling'],
                    'top_frustrations': ['Expensive pricing ($20-45/mo)', 'Steep learning curve', 'Overkill for simple use cases'],
                    'switching_patterns': 'Users come from Excel, Google Sheets. Some churn to Notion for simpler use cases or cost.'
                },
                'recent_launches': ['AI-powered field generation', 'Interface designer 2.0', 'Advanced automations', 'Enterprise admin controls'],
                'strategic_focus': 'AI features and enterprise no-code platform',
                'target_signals': {
                    'customer_types': ['Operations teams', 'Product teams', 'Marketing teams', 'Data-heavy workflows'],
                    'size_focus': 'Mid-market to Enterprise (50-1000+ employees)'
                },
                'growth_motion': 'Hybrid - PLG for teams, Sales-led for enterprise',
                'target_market': 'Operations and data-heavy teams',
                'competitive_advantages': ['Most powerful databases', 'Best automation features', 'Enterprise-grade security', 'Strong for structured workflows', 'Extensive API'],
                'potential_gaps': ['Premium pricing creates mid-market gap', 'Weak at unstructured docs', 'Complex for simple needs', 'Interface can feel dated', 'High learning curve'],
                'strategic_vulnerabilities': ['Price sensitivity in downturn', 'Notion improving database features', 'Microsoft competing in no-code space']
            }
        },
        'clickup': {
            'name': 'ClickUp',
            'analysis': {
                'core_value_prop': 'One app to replace them all',
                'pricing': {
                    'tiers': ['Free: $0', 'Unlimited: $7/user/mo', 'Business: $12/user/mo', 'Enterprise: Custom'],
                    'starting_price': '$0',
                    'has_free_tier': True,
                    'enterprise_pricing': 'Custom'
                },
                'key_features': ['Tasks and projects', 'Time tracking', 'Goals', 'Docs', 'Dashboards', 'Automations', 'Whiteboards', 'Chat', 'Everything view'],
                'customer_sentiment': {
                    'rating': '4.7/5',
                    'review_count': '8,912',
                    'top_loved': ['Feature-rich platform', 'Best value for money', 'Highly customizable'],
                    'top_frustrations': ['Overwhelming feature set', 'Cluttered interface', 'Setup requires significant time'],
                    'switching_patterns': 'Users come from Asana, Trello. Power users frustrated by simplicity switch TO ClickUp. Some churn to Notion/Monday for simplicity.'
                },
                'recent_launches': ['ClickUp Brain AI', 'Universal Search', 'Whiteboards 2.0', 'Advanced automations', 'Chat improvements'],
                'strategic_focus': 'AI integration and becoming the everything app',
                'target_signals': {
                    'customer_types': ['Agencies', 'Fast-growing startups', 'Remote teams', 'Power users'],
                    'size_focus': 'SMB to Mid-market (10-500 employees)'
                },
                'growth_motion': 'Aggressive PLG with viral marketing',
                'target_market': 'Productivity enthusiasts and growing teams',
                'competitive_advantages': ['Lowest pricing ($7-12/mo)', 'Most features in one platform', 'Highly customizable', 'Strong marketing', 'Fast innovation'],
                'potential_gaps': ['Feature overload causes overwhelm', 'Cluttered interface', 'Steep learning curve', 'Setup complexity', 'Jack of all trades perception'],
                'strategic_vulnerabilities': ['Complexity driving users away', 'Trying to be everything risks being master of nothing', 'Notion and Asana both targeting their segments']
            }
        }
    },
    'comparison': {
        'market_overview': 'Three distinct approaches competing: Notion (flexible docs), Airtable (structured databases), ClickUp (everything app). Clear pricing tiers: ClickUp value ($7-12), Notion balanced ($8-15), Airtable premium ($20-45). Each has loyal following but also clear weaknesses creating opportunities.',
        'pricing_comparison': {
            'range': '$0-45/user/mo for paid tiers',
            'positioning': 'ClickUp: Value leader, Notion: Balanced, Airtable: Premium'
        },
        'feature_gaps': [
            'Notion: Weak automation and complex database relationships',
            'Airtable: Poor at unstructured docs and knowledge management',
            'ClickUp: Overwhelming complexity, lacks focus',
            'None excel at: Simple yet powerful, AI-first integration'
        ],
        'market_opportunities': [
            'Mid-tier pricing ($15-18/mo) between Notion and Airtable',
            'Teams outgrowing Notion databases but intimidated by Airtable cost',
            'Users wanting ClickUp power without the complexity',
            'AI-native docs + databases (no one does this well yet)',
            'Better onboarding and time-to-value than ClickUp'
        ],
        'strategic_recommendations': [
            'Price at $15-18/mo: Signal quality over ClickUp, accessible vs Airtable',
            'Core positioning: "Notion simplicity + Airtable power" - best of both worlds',
            'Avoid ClickUp feature trap: Focus on core use cases done excellently',
            'Emphasize AI-first approach: Build AI into core product, not bolted on',
            'Target frustrated ClickUp users (complexity) and Notion power users (database limits)',
            'Lead with "Setup in minutes, not weeks" vs ClickUp multi-week onboarding',
            'Build migration tools from all three, especially Notion and Airtable'
        ],
        'threats': [
            'Notion has strong brand momentum and could improve databases',
            'Airtable has deep enterprise relationships and funding',
            'ClickUp aggressive pricing and marketing machine'
        ],
        'advantages': [
            'Late mover can learn from all their mistakes',
            'Clear gap between Notion simplicity and Airtable power',
            'Growing user frustration with current options',
            'AI opportunity: Build AI-native, not retrofitted'
        ]
    }
}
