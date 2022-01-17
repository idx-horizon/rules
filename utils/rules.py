import config

def is_relationship(param):
#	valid = ['father','mother', 'partner', 'husband', 'wife']
	valid = config.valid_relationships
	if not param:
		param = ''

	return 1 if param.lower() in valid else 0

def is_category_code(param):
	valid =  ['01','02', '03']
	if not param:
		param = ''

	return  1 if param.lower() in valid else 0

def is_over_15(param):
	if not param:
		return 0
	elif param>15:
		return 1
	elif param >=0 and param<16:
		return -5
	else:
		return 0
