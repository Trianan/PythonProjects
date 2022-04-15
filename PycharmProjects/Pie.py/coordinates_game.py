# Coordinate Map Game (2D) Version 0.1 by: Tristin Manson

# Initialization:
x, y = 0, 0
coordinates = f"({x},{y})"
player_health = 3
player_inventory = []

print('Initializing...')
print(coordinates)
print('(Type EX to exit game.)')

# Entering Map:
while True:

    # Death conditions:
    if player_health == 0:
        print('\nYou died.')
        break
    elif player_health == 1:
        print('\nYou are badly injured.')
        if 'health-pack' in player_inventory:
            print('You treat your wounds with a health-pack.')
            player_inventory.remove('health-pack')
            player_health += 2
            print(f'Health: {player_health}\n')

    # Movement System:
    direction = input('Direction: N/S/E/W: ').lower()

    if direction == 'e':
        if x < 15:
            x += 1
        else:
            print('Cannot go further east.')

    elif direction == 'w':
        if x > -15:
            x -= 1
        else:
            print('Cannot go further west.')

    elif direction == 'n':
        if y < 15:
            y += 1
        else:
            print('Cannot go further north.')

    elif direction == 's':
        if y > -15:
            y -= 1
        else:
            print('Cannot go further south.')

    # Exit/Invalid Input:
    elif direction == 'ex':
        break

    else:
        print('Invalid input')

    # Location Tracker:
    coordinates = f"({x},{y})"
    print(coordinates)

    # Locations/Encounters
    # Jimmy the Sword-Bearer:
    if x == 6 and y == 10:
        print('\nYou encounter Jimmy! He gives you a sword.')
        player_inventory.append('sword')
        print(f'{player_inventory}\n')

    # Health-Pack:
    elif x == 3 and y == 3:
        print('\nYou pick up a health-pack.')
        player_inventory.append('health-pack')
        print(f'{player_inventory}\n')

    # Vampire 1:
    elif x == -5 and y == -8:
        print('\nYou encounter a ravenous vampire!')
        if 'sword' in player_inventory:
            print('It was a tough fight, but you successfully killed the vampire with your sword.')
            player_health -= 2
            print(f'Health: {player_health}\n')
        else:
            print('Unable to defend yourself, the vampire easily drains all your blood.')
            player_health -= 3

    # Zombie 1:
    elif x == -12 and y == -10:
        print('\nYou encounter a zombie!')
        if 'sword' in player_inventory:
            print('You successfully killed the zombie with your sword.')
            player_health -= 1
            print(f'Health: {player_health}\n')
        else:
            print('Unable to defend yourself, the zombie eats your brains.')
            player_health -= 3

    # Zombie 2 (exit):
    elif x == -5 and y == -15:
        print('\nYou encounter a zombie blocking the exit.')
        if 'sword' in player_inventory:
            print('You successfully killed the zombie with your sword, and successfully leave the map.')
            player_health -= 1
            print(f'Health: {player_health}')
            break
        else:
            print('Unable to defend yourself, the zombie eats your brains.')
            player_health -= 3
