import utils.config as config

NOT_PROVIDED = (0, 'NOT_PROVIDED')

def is_relationship(param):
	if not param: return  NOT_PROVIDED

	return (1, 'VALID_RELATIONSHIP') if param.lower() in config.valid_relationships else (-1, 'NOT_RELATIONSHIP')


def is_category_code(param):
	if not param: return NOT_PROVIDED

	return  (1,'VALID_CATEGORY_CODE') if param.lower() in config.valid_category_codes else (-1, 'NOT_CATEGORY_CODE')


def in_range(param, min_value=0, max_value=15):
	if not param or param == '': return NOT_PROVIDED
	try:
		param=float(param)
	except:
		return (0, 'NON_NUMERIC_VALUE')

	if param >= min_value and param <= max_value:
		return (1,'VALID_IN_RANGE')
	elif not isinstance(param, (int,float)):
		return (0, 'NON_NUMERIC_VALUE')
	else:
		return (-5, 'NOT_IN_RANGE')
