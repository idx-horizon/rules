import sys
import os
import datetime
import csv
import random
import pandas

datalists = {
	'bad': ['', 'bad', 'invalid', 'not known', 'n/a', '~', '\"', '\''],

	'relationship': ['father','mother', 'boyfriend', 'girlfriend','ex'],

	'nicl':         ['da','csa','kc','other'],

	'summary': ['general',
		    'The KW is important',
		    'The man sliced the boyfriend',
		    'No keywords'],

	'other' : []
}
def load(fn):
	return pandas.read_csv(fn,dtype='str').fillna('').to_dict(orient='records')

def get_random(category, error_rate, lower, upper):

	bad = random.randrange(0,100)
	if bad < error_rate:
		lst = datalists['bad']
		return lst[random.randrange(0,len(lst))]
	else:
		if category == 'num':
			return random.randrange(lower, upper)
		else:
			lst = datalists[category]
			return lst[random.randrange(0,len(lst))]
def getnow(fmt='%H:%M:%S %d-%b-%Y'):
	return datetime.datetime.now().strftime(fmt)

def  make_data(fn, limit=5):
	print('\n** {} - Start: make_data({}, limit={})\n'.format(getnow(), fn,limit))
	with open(fn,'w', newline='') as fh:
		for i in range(1,limit+1):
			data = {'id': i,
				'v_age':          get_random('num', 15, 0, 50),
				'o_age':          get_random('num', 15, 5, 25),
				'category_code':  get_random('num', 20, 1, 100),
				'relationship':   get_random('relationship', 20, None, None),
				'nicl':           get_random('nicl',    10, None, None),
				'summary':        get_random('summary', 10, None, None)
			}
			if i == 1:
				dw = csv.DictWriter(fh,fieldnames=list(data.keys()), quoting=csv.QUOTE_ALL)
				dw.writeheader()
			dw.writerow(data)
			if i < 4 or limit-i <3:
				print(data)
	print('\n** {} - End: make_data({},limit={})'.format(getnow(), fn,limit))


if __name__ == '__main__':
	if len(sys.argv):
		fn = sys.argv[1]
		limit = int(sys.argv[2])
	else:
		fn = 'testdata/test_10.csv'
		limit = 10

	make_data(fn, limit)
	data = load(fn)
	print('** data list (recs={})\n'.format(len(data)))

