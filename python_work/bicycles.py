# FRIEND GREETING SOFTWARE

# This section initializes name_index to 0, so the next section iterates 
#from the first name in the list.
name_index = 0
names = ['Damon', 'Jesse', 'Viv', 'Cheyenne']

# This loop takes each name, inputs it into the greeting template, and 
# prints the resulting message. 
# It then adds 1 to the index value, which changes the next iterations' 
# index to the next name's index value.
# This loop continues until all names in the list have been inputted and 
# printed, and then it breaks the loop. 
while True:
    message = f'Hello {names[name_index]}.'
    print(message)
    name_index = name_index + 1
    if name_index > 3:
        break
 
