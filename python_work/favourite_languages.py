favourite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favourite_languages.items():

	if len(languages) == 1:
		plur = 'language is'
	else:
		plur = 'languages are'

	print(f"\n{name.title()}'s favourite {plur}:")
	for language in languages:
		print(f"\t{language.title()}")
