
import csv
import random
import pandas

def load(fn):
	return pandas.read_csv(fn,dtype='str').fillna('').to_dict(orient='records')

def get_random(badratio, lower, upper,category):
	bad_list = ['', 'bad', 'invalid']
	relationship_list = ['father','mother', 'boyfriend', 'girlfriend','ex']
	nicl_list = ['da','csa','kc','other']

	bad = random.randrange(0,100)
	if bad < badratio:
		return bad_list[random.randrange(0,len(bad_list))]
	else:
		if category == 'num': 
			return random.randrange(lower, upper)
		elif category=='rel':
			return relationship_list[random.randrange(0,len(relationship_list))]
		elif category=='nicl':
			return nicl_list[random.randrange(0,len(nicl_list))]

def  make_data(fn='testdata.csv', limit=5):
	with open(fn,'w', newline='') as fh:
		for i in range(1,limit+1):
			data = {'id': i,
				'v_age':          get_random(15, 0, 50, 'num'),
				'o_age':          get_random(15, 5, 25, 'num'),
				'relationship':   get_random(20, None, None, 'rel'),
				'nicl':           get_random(10, None, None, 'nicl'),
				'category_code':  str(get_random(20,1,100, 'num'))
			}
			if i == 1:
				dw = csv.DictWriter(fh,fieldnames=list(data.keys()), quoting=csv.QUOTE_ALL)
				dw.writeheader()
			dw.writerow(data)
			if i < 5 or limit-i <5:
				print(data)


if __name__ == '__main__':
	fn = 'testdata.csv'
	make_data(fn, 5)
	for i in load(fn): print(i)

