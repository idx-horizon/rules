import re

def synonym_rings(word):
	x = {
		'PERSON': ['he','she','him','her','man','woman'],
		'STAB': ['STAB', 'STABBED', 'STABBING',
			 'CUTTING','CUTS',  'CUT',
			 'SLICE', 'SLICING', 'SLICED',
			 'PIERCE',
			 'GOUGE'],
		'ONLINE_PLATFORM': ['facebook','snapchat','instagram', 'twitter']
	}
	return r'(' + '|'.join(x[word]) + ')'

def get_regexes():
	return {
		'multi_space':    re.compile(r'\s+'),
		'anon_numbers':   re.compile(r'[0-9]'),
		'trailing_space': re.compile(r'^\s+|\s+$'),
		'upper_test':     re.compile(r'\btests?\b', re.IGNORECASE),
		'STAB':           re.compile(r'\b'+synonym_rings('STAB')+r'\b', re.IGNORECASE ),
		'PERSON':         re.compile(r'\b'+synonym_rings('PERSON')+r'\b', re.IGNORECASE ),
		'ONLINE': re.compile(r'\b'+synonym_rings('ONLINE_PLATFORM')+r'\b', re.IGNORECASE )
	}

def get_rulesets():
 return  [
		{'rex': 'multi_space',     'replace_with': ' ' },
		{'rex': 'anon_numbers',    'replace_with': '0'},
		{'rex': 'trailing_space',  'replace_with': ''},
		{'rex': 'upper_test',      'replace_with': 'TEST'},
		{'rex': 'STAB',            'replace_with': '[STAB]'},
		{'rex': 'PERSON',          'replace_with': '[PERSON]'},
		{'rex': 'ONLINE', 'replace_with': '[ONLINE]'}
	]
