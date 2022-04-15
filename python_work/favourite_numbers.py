favourite_numbers = {
    'jim': [7, 14, 21],
    'sam': [13, 9],
    'bob': [4]
    }

for name, numbers in favourite_numbers.items():

    if len(numbers) == 1:
        plur = 'number is'
    else:
        plur = 'numbers are'
    print(f"\n{name.title()}'s favourite {plur}:")

    for number in numbers:
        print(number)

