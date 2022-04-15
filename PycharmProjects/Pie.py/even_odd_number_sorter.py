# EVEN & ODD NUMBERS:
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(f'Numbers: {list}')

# Inputs a list of consecutive integers, and sorts them alternatively into two lists:
even_numbers = []
odd_numbers = []
n = 0
for number in list:
    if n == 0:
        n = n + 1
        odd_numbers.append(number)
    elif n == 1:
        n = n - 1
        even_numbers.append(number)
print(f'Even numbers: {even_numbers} Odd numbers: {odd_numbers}')
# Outputs two lists containing even and odd numbers respectively.

# More list fuckery...
print()
list.append(even_numbers)
print(list)
list.append(odd_numbers)
print(list)
print(len(list[17] + list[18]))





