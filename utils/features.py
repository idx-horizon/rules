import utils.rules as RULE
features = {
 'adr-119': [
        {'description': 'victim_age',   'function':  RULE.is_over_15, 'params': 'v_age'},
        {'description': 'offender_age', 'function':  RULE.is_over_15, 'params': 'o_age'},
        {'description': 'relationship', 'function':  RULE.is_relationship, 'params': 'relationship'},
        {'description': 'category_code', 'function': RULE.is_category_code, 'params': 'category_code'},
        {'description': 'victim_age_range', 'function': RULE.in_range, 'params': 'v_age'}
  ],
  'adr-160': [
	{'description': 'category_code', 'function': RULE.is_category_code, 'params': 'category_code'}
  ]
}
