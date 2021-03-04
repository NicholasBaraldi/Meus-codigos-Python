cat = {'size': 'fat', 'color': 'black'}

if 'age' not in cat:
	cat['age'] = 10

print(cat)

cat.setdefault('name', 'rex')

print(cat)