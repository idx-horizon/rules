import logging
import os

import utils.rules as rules
from utils.features import features
from data.dataset import testdata

from utils.utils import  MyLog, NZ, traffic_light


def run(adr):
	mylog=MyLog(__name__, logging.INFO)
	mylog.info('** applying feature rules for {}'.format(adr))

	if adr not in features.keys():
		mylog.error('ERROR: No features defined for ADR: {}'.format(adr))
		return None

	for d in testdata:
		mylog.info('\n** Test case: [{}]'.format(d))
		for f in features[adr]:
			func=f['function']
			args=d.get(f['params'],'_missing_'+f['params'])
			result= func(args) if not str(args).startswith('_missing_') else 0
			mylog.info('{:<20} {:>2} - {:<15}: {}({:>2})'.format(
								traffic_light(result),
								result,
								f['description'],
								func.__name__,
								NZ(args)
				 ))

	mylog.info('** end')

if __name__ == '__main__':
	os.system('clear')
	run('adr-119')
