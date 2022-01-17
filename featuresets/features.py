from rulesets import rules 
features = {
        "f1": {'description': 'victim_age',   'function':  rules.f_age, 'params': 'v_age'},
        "f2": {'description': 'offender_age', 'function':  rules.f_age, 'params': 'o_age'},
        "f3": {'description': 'relationship', 'function':  rules.f_rel, 'params': 'relationship'},
        "f4": {'description': 'category_code', 'function': rules.f_catcode, 'params': 'category_code'}
}
