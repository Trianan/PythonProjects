menu = {
	'appetizers': ['fries', 'deep-fried pickles', 'onion-rings'],
	'meals': ['cheeseburger', 'salad', 'steak', 'chicken-nuggets'],
	'deserts': ['ice-cream', 'milkshake'],
	}

for section, foods in menu.items():
	print(f"{section.title()}:")

	for food in foods:
		print(f"\t{food.title()}")
	print()





    
