# ZOMBIE CHAPEL OF SPOOKINESS: Version 0.1

# Introduction & Initialization:
player_inventory = []
# This is meant to work with the "sword" and "health potion" items, and zombie encounters will check if these items
# are in inventory.
player_location = 'pathway'
# player_location is meant to work with "while player_location == x" loops. Feature not implemented yet.

print('You walk down a cobblestone pathway towards an old chapel.')
answer = input('\tDo you enter the chapel? y/n: ').lower()

# Room 1:
if answer == 'y':
    player_location = 'room1'
    # This line is where "while player_location == 'room1' loop will begin:
    print('''\nYou open the heavy oak doors and enter a long room. 
Stained glass windows scatter a cascade of colour across the worn hardwood floor.

To your north, you see a door that appears to lead outside to the other side of the chapel.
A hallway leads west, further into the chapel.
You see a chest in the southeast corner of the room.
''')

direction = input("Where do you go? n/w/se: ").lower()

# North:
if direction == 'n':
    print('You walk directly towards the door, and open it, leading outside. A zombie kills your ass. \nToo bad you '
          'did not have anything to defend yourself.')

# Hallway:
elif direction == 'w':
    print('You walk down the dark hallway into a wide room with rows of pews. \nThe ceiling of the hallway leading '
          'into the room collapses, preventing you from going back the way you came in.')

# Write: elif direction == se: get health potion from chest and somehow loop to direction prompt.