
#1: Imports defined name into the formatted-string value of message, while also formatting message to display over 3 lines. 

name = "Joseph Stalin"
message = f'{name} once said, \n\t"The death of one man is a tragedy. \n\tThe death of millions is a statistic."'
print(message)

#2: Takes a defined value for name, which includes a lot of whitespace, and removes whitespace using .strip() functions while displaying each iteration. 

name = " \n\tjoe\n\t\t   "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())