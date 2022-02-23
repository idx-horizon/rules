import utils.rules as RULE

features = {
    'online-crime': [
	{'description': 'keyword_online_platform',
	 'function': RULE.has_keyword,
	 'dargs': 'summary',
	 'fargs': (5, 0, -5,'[ONLINE]')
	},
    ],
    'adr-119': [
        { 'description': 'victim_age_over_15',
          'function':  RULE.in_range,
          'dargs': 'v_age',
          'fargs': (16,999)
        },
        { 'description': 'offender_age_over_15',
          'function':  RULE.in_range,
          'dargs': 'o_age',
          'fargs': (16,999)
        },
        { 'description': 'relationship',
          'function':  RULE.is_relationship,
          'dargs': 'relationship',
          'fargs': ()
        },
        { 'description': 'category_code',
          'function': RULE.is_category_code,
          'dargs': 'category_code'
        },
    ],

    'adr-160': [
        { 'description': 'category_code', 
          'function': RULE.is_category_code, 
          'dargs': 'category_code' 
        },
        { 'description': 'is_stab_like',
          'function': RULE.has_keyword,
          'dargs': 'summary',
	  'fargs': (3,0,-3,'[STAB]')
        }
    ]

}
