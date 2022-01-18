import logging
import os
from collections import Counter

import utils.rules as rules
from utils.features import features
from data.dataset import testdata

from utils.utils import  MyLog, NZ, traffic_light, convertTuple

def  report_summary(results):
	c = Counter()
	c.update([traffic_light(x) for x in results])
	c['TOTAL_NEGATIVE'] = sum([x[0] for x in results if x[0] < 0])
	c['TOTAL_POSITIVE'] = sum([x[0] for x in results if x[0] > 0])

	line = ''
	for  ele in c: 
		line+= '{} = {}  '.format(ele, c[ele])

	return line

def run(adr):
	mylog=MyLog(__name__, logging.INFO)
	mylog.info('\n** Applying feature rules for {}'.format(adr))

	if adr not in features.keys():
		mylog.error('** ERROR: No features defined for ADR: {}'.format(adr))
		return None

	for d in testdata:
		mylog.info('\n** Test case: [{}]'.format(d))
		summary = []
		for f in features[adr]:
			func=f['function']
			dargs = d.get(f['dargs'],'__MISSING__')
			fargs = f.get('fargs',())
			result= func(dargs, *fargs) if not str(dargs).startswith('__MISSING__') else  (0, 'NOT_PROVIDED')
			mylog.info('\t{:<20} {:>2} {:<20} - {:<25}: {}({:>2},{})'.format(
								traffic_light(result),
								result[0],
								result[1],
								f['description'],
								func.__name__,
								NZ(dargs),
								convertTuple(fargs)
				 ))
			summary.append(result)

		report_line = report_summary(summary)
		print('** SUMMARY: {}'.format(report_line))

	mylog.info('\n** End **')

if __name__ == '__main__':
	os.system('clear')
	run('adr-119')
