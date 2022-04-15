movement_on = True
print('''Controls:

brake on/off - Engages or disengages brakes.
stop - Puts both tracks into neutral.
forward - Moves forward. (Brakes must be disengaged)
right - Turns robot clockwise.
left - Turns robot anticlockwise. 
reverse - Moves in reverse. (Must already be stopped before use)
''')

left_track = 'neutral'
right_track = 'neutral'
brake = 'off'
print('START')

while movement_on == True:

    print(f'''Left Track: {left_track}
Right Track: {right_track}
Brake: {brake}
    ''')
    user_input = input(">: ").lower()

    if user_input == 'brake off':
        brake = 'off'
        print('Brake disengaged...')
    elif user_input == 'brake on':
        brake = 'on'
        print('Brake engaged...')

    elif user_input == 'stop':
        left_track = 'neutral'
        right_track = 'neutral'
        if brake == 'on':
            print('Coming to a complete stop.')
        else:
            print('Coasting...')


    elif brake == 'off':

        if user_input == 'forward':
            print('Moving straight forward.')
            left_track = 'forward'
            right_track = 'forward'
        elif user_input == 'right':
            left_track = 'forward'
            right_track = 'neutral'
            print('Turning clockwise...')
        elif user_input == 'left':
            left_track = 'neutral'
            right_track = 'forward'
            print('Turning counterclockwise...')

        else:
            print('Please disengage brake.')


