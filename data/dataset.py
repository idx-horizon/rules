import gen_data

def load_data(fn):
	return gen_data.load(fn)

testdata = [
	{'id': 1, 'v_age': 15, 'o_age':23, 'relationship': 'Partner', 'category_code': '99'},
	{'id': 2, 'v_age': 23, 'o_age':10, 'relationship': 'Stranger','category_code': '02'},
	{'id': 3, 'v_age': None, 'o_age':18, 'relationship': 'Husband'},
	{'id': 4, 'v_age': '', 'o_age':18, 'relationship': None, 'category_code': '01'},
	{'id': 5, 'v_age': ''},
	{'id': 6, 'v_age': 'rubbish_data'},
	{'id': 7, 'v_age': 15.5, 'o_age': '17.2'},
	{'id': 8, 'v_age': 4, 'o_age': 22, 'relationship': None, 'category_code': '79'},
	{'id': 9, 'v_age': 1, 'o_age': 18, 'relationship': 'rubbish', 'category_code': '21'},
	{'id': 10, 'v_age': 41, 'o_age': 14, 'relationship': 'boyfriend', 'category_code': '1'},
	{'id': 11, 'v_age': 38, 'o_age': 24, 'relationship': 'ex', 'category_code': '28'},
	{'id': 12, 'v_age': 0, 'o_age': 14, 'relationship': 'ex', 'category_code': '42'},
]
