bob = {
	'full_name': 'bob johnson',
	'age': 23,
	'sex': 'male',
	'location': 'new york',
	}

jim = {
	'full_name': 'jim jones',
	'age': 35,
	'sex': 'male',
	'location': 'denver',
	}
sam = {
	'full_name': 'sam bamm',
	'age': 21,
	'sex': 'female',
	'location': 'salt lake city',
	}

people = [bob, jim, sam]
for person in people:
	print(person['full_name'].title())
	for key, value in person.items():
		age = person['age']
		sex = person['sex']
		location = person['location']
	print(f"\tAge: {age}, Sex: {sex}, Location: {location.title()}\n")
