import logging
import os
from termcolor import colored

import features.rules
from data.dataset import testdata

def MyLog(name,level):
	log = logging.Logger(name)
	log.addHandler(logging.StreamHandler())
	log.setLevel(level)
	return log

def NZ(arg):
	return arg if arg else ''


def traffic_light(param):
	if param>0:
		return colored('POSTIVE','green')
	elif param<0:
		return colored('NEGATIVE','red')
	else:
		return colored('NEUTRAL','yellow')

features = {
	"f1": {'description': 'victim_age',   'function': features.rules.f_age, 'params': 'v_age'},
	"f2": {'description': 'offender_age', 'function': features.rules.f_age, 'params': 'o_age'},
	"f3": {'description': 'relationship', 'function': features.rules.f_rel, 'params': 'relationship'},
	"f4": {'description': 'category_code', 'function':features.rules.f_catcode, 'params': 'category_code'}
}

if __name__ == '__main__':
	_ = os.system('clear')
	mylog=MyLog(__name__, logging.INFO)

	mylog.debug('Start')
	for d in testdata:
		mylog.info('\n** Test case: [{}]'.format(d))
		for f in features:
			func=features[f]['function']
			args=d.get(features[f]['params'],'_missing_'+features[f]['params'])
			result= func(args) if not str(args).startswith('_missing_') else 0
			mylog.info('{:<20} = {:<2} - {:<15} = {:>2} - {}({:>2})'.format(
								traffic_light(result),
								f,
								features[f]['description'],
								result,
								func.__name__,
								NZ(args), ))

	mylog.debug('End')

