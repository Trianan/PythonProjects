cities = {
	'moscow': {
		'country': 'russia',
		'population': '11.9 million',
		'fact': 'location of the Red Square.',
		},

	'new york': {
		'country': 'united states',
		'population': '8.4 million',
		'fact': 'location of the U.N headquarters.',
		},

	'toronto': {
		'country': 'canada',
		'population': '2.9 million',
		'fact': 'location of the CN tower.',
		}
	}

for city, info in cities.items():
	print(f"{city.title()}:")

	for value in info.values():
		country = info['country'].title()
		population = info['population']
		fact = info['fact']
		
	print(f"Country: {country}, Population: {population}")
	print(f"Fun Fact: {fact}\n")

