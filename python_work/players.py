players = ['charles', 'martina', 'michael', 'florence', 'eli']

print('The first three players are:')
for player in players[:3]:
	print(player.title())

print('\nThe middle three are:')
for player in players[1:4]:
	print(player.title())

print('\nThe last three are:')
for player in players[-3:]:
	print(player.title())