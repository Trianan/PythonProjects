favourite_places = {
    'jim': ['berlin', 'copenhagen'],
    'sam': ['moscow', 'st. petersburg', 'tokyo'],
    'bob': ['austin'],
    }

for name, places in favourite_places.items():
    print(f"\nName: {name.title()}")

    if len(places) == 1:
        plur = 'Place'
    else:
        plur = 'Places'

    print(f"Favourite {plur}:")
    for place in places:
        print(f"{place.title()}")
