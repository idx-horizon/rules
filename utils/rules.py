import utils.config as config

def is_relationship(param):
	if not param:
		param = ''

	return 1 if param.lower() in config.valid_relationships else 0

def is_category_code(param):
	if not param:
		param = ''

	return  1 if param.lower() in config.valid_category_codes else 0

def is_over_15(param):
	if not param:
		return 0
	elif param>15:
		return 1
	elif param >=0 and param<16:
		return -5
	else:
		return 0

def in_range(param, min_value=0, max_value=15):
	if not param:
		return 0
	if param in range(min_value, max_value):
		return 1
	else:
		return 0