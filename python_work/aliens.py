aliens = []

for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print('...')

print(f"Total number of aliens: {len(aliens)}")