import logging
import os

import utils.rules as rules
from utils.features import features
from data.dataset import testdata

from utils.utils import  MyLog, NZ, traffic_light, convertTuple


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
			dargs = d.get(f['dargs'],'_missing_'+f['dargs'])
			fargs = f.get('fargs',())
			result= func(dargs, *fargs) if not str(dargs).startswith('_missing_') else  (0, 'NOT_PROVIDED')
			mylog.info('\t{:<20} {:>2} {:<20} - {:<25}: {}({:>2},{})'.format(
								traffic_light(result),
								result[0],
								result[1],
								f['description'],
								func.__name__,
								NZ(dargs), convertTuple(fargs)
				 ))

	mylog.info('** end')

if __name__ == '__main__':
	os.system('clear')
	run('adr-119')
