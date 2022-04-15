x,y,z = 0,0,0
coordinates = f"({x},{y},{z})"

print(coordinates)

while True:

    direction = input('(E for Exit) Direction: F/B/R/L/U/D: ').lower()
    if direction == 'f':
        x += 1
    elif direction == 'b':
        x -= 1
    elif direction == 'r':
        y += 1
    elif direction == 'l':
        y -= 1
    elif direction == 'u':
        z += 1
    elif direction == 'd':
        z -= 1

    elif direction == 'e':
        break
    else:
        print('Invalid input')
          
    coordinates = f"({x},{y},{z})"
    print(coordinates)
