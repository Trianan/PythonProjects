
direction = ''
location = 'porch'
movement = ''
inventory = []
k = 0

print('You must find the briefcase inside the house.')

location_house = True
while location_house is True:



    if location == 'porch':
        print('You are on the front porch. There is a door to your west, and you can leave the property by going east.')
        movement = input('N/E/S/W:').upper()
        if movement == 'W':
            print('You go through the door.')
            location = 'living room'
        elif movement == 'E':
            if 'briefcase' in inventory:
                print('You walk down the front steps of the porch, holding the briefcase.')
                location = 'leave'
            else:
                print('You must find the briefcase before you can leave!')
        elif movement in ['N','S']:
            print('You cannot go there!')
        else: print('What?')

    elif location == 'bathroom':
        print('You are in the bathroom. The living room is to your east.')
        if 'knife' not in inventory:
            print('You find a knife in the sink.')
            inventory.append('knife')
            print(inventory)
        movement = input('N/E/S/W:').upper()

        if movement == 'E':
            print('You leave the bathroom.')
            location = 'living room'
        elif movement in ['N','S','W']:
            print('You cannot go there!')
        else:
            print('What?')

    elif location == 'kitchen':
        k += 1
        print('You are in the kitchen. The bedroom is to your west, and the living room is to your south.  ')
        if k < 2:
            print('A zombie climbs out of the cupboard.')
            if 'knife' in inventory:
                print('You stab the zombie through the eye socket, killing it instantly.')
            else:
                print('The zombie shambles over to you, and bites your face off. You get eaten alive.')
                break
                location_house = False

        movement = input('N/E/S/W:').upper()
        if movement == 'W':
            location = 'bedroom'
            print('You enter the doorway leading into the bedroom.')
        elif movement == 'S':
            print('You walk into the living room.')
            location = 'living room'
        elif movement in ['N','E']:
            print('You cannot go there!')
        else:
            print('What?')

    elif location == 'living room':
        print('You are in the living room. To your west is the bathroom, kitchen is to your north, and the porch is east.')
        movement = input('N/E/S/W:').upper()
        if movement == 'W':
            print('You enter the doorway leading into the bathroom.')
            location = 'bathroom'
        elif movement == 'N':
            print('You walk into the kitchen.')
            location = 'kitchen'
        elif movement == 'E':
            print('You open the front door and go outside.')
            location = 'porch'
        elif movement == 'S':
            print('You cannot go there!')
        else:
            print('What?')

    elif location == 'bedroom':
        print('You are in the bedroom. To your east is the kitchen.')
        if 'briefcase' not in inventory:
            print('You find the briefcase in the corner of the room.')
            inventory.append('briefcase')
            print(inventory)
        movement = input('N/E/S/W:').upper()
        if movement == 'E':
            print('You leave the bedroom.')
            location = 'kitchen'
        elif movement in ['N', 'S', 'W']:
            print('You cannot go there!')
        else:
            print('What?')

    elif location == 'leave':
        print('You leave the house.')
        location_house = False
    else:
        print('Where are you???')










