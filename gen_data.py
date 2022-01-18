
import random

def get_random(badratio, lower, upper,category):
	bad = random.randrange(0,100)
	bad_list = ['', None, 'bad', 'invalid']
	relationship_list = ['father','mother', 'boyfriend', 'girlfriend','ex']

	if bad < badratio:
		return bad_list[random.randrange(0,len(bad_list))]
	else:
		if category == 'num': 
			return random.randrange(lower, upper)
		elif category=='rel':
			return relationship_list[random.randrange(0,len(relationship_list))]

def  generate(limit):
	for i in range(1,limit+1):
		data = {'id': i,
			'v_age': get_random(15, 0, 50, 'num'),
			'o_age': get_random(15, 5, 25, 'num'),
			'relationship': get_random(20, None, None, 'rel'),
			'category_code':  str(get_random(20,1,100, 'num'))
		}
		print(data)

if __name__ == '__main__':
	generate(5)
#[{'id': 1, 'v_age': 15, 'o_age': 23, 'relationship': 'Partner', 'category_code': '99'}]
