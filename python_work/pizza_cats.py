my_pizzas = ['pepperoni', 'deluxe', 'canadian']

friend_pizzas = my_pizzas[:]

my_pizzas.append('4-cheese')
friend_pizzas.append('meatlovers')
print(f'My favourite pizzas are: {my_pizzas}')
print(f'My friends favourite pizzas are: {friend_pizzas}.')

for pizza in my_pizzas[:2]:
	print(pizza)
for pizza in friend_pizzas[:]:
	print(pizza)



