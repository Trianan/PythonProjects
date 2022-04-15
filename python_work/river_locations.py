river_locations = {
    'nile': 'egypt',
    'mississippi': 'the united states',
    'rhine': 'germany',
    }

for river, country in river_locations.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in river_locations.keys():
    print(river)

for country in river_locations.values():
    print(country)