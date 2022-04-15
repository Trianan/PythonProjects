list = ['a','b','c']
list_b = []

while len(list) > 0:
    letter = (list.pop(-1)) + '12'
    list_b.append(letter)
    
print(list)
print(list_b)
