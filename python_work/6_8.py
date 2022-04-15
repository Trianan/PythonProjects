pet_0 = {'animal': 'cat', 'owner_name': 'jimothy'}
pet_1 = {'animal': 'dog', 'owner_name': 'sam'}
pet_2 = {'animal': 'bird', 'owner_name': 'terry'}
pet_3 = {'animal': 'cat', 'owner_name': 'gaston'}

pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
	print(f"Animal Type: {pet['animal']}")
	print(f"\tOwner's Name: {pet['owner_name'].title()}\n")