available_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'bacon', 'pepperoni']

requested_toppings = ['mushrooms', 'ice cream', 'extra cheese']

for requested_topping in requested_toppings:

	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"We do not have {requested_topping}.")
		
print('Finished.')