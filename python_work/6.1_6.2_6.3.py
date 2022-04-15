# 6.3:
python_words = {
    'print()': 'Prints value on terminal.',
    'len()': 'Returns count of elements in list.',
    '.append()': 'Adds item to end of list.',
    '.insert()': 'Adds item to list at specified index.',
    'del': 'Deletes value or element.',
    '.items()': 'Returns a list of key-value pairs from a dictionary.',
    '.keys()': 'Returns a list of only the keys from a dictionary.',
    '.values()': 'Returns a list of only the values from a dictionary.',
    'set()': 'Returns a list of only the unique items in a collection.',
    'sorted()': 'Returns a sorted version of a list.'
    }

for word, definition in python_words.items():
    print(f"{word}:\n\t{definition}\n")

