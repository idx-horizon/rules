import utils.rules 
features = {
 'adr-119': [
        {'description': 'victim_age',   'function':  utils.rules.is_over_15, 'params': 'v_age'},
        {'description': 'offender_age', 'function':  utils.rules.is_over_15, 'params': 'o_age'},
        {'description': 'relationship', 'function':  utils.rules.is_relationship, 'params': 'relationship'},
        {'description': 'category_code', 'function': utils.rules.is_category_code, 'params': 'category_code'}
  ],
  'adr-160': [
	{'description': 'category_code', 'function': utils.rules.is_category_code, 'params': 'category_code'}
  ]
}
