# Darian Moody's demonstration of ".all()" method:

# These set the values of 3 separate variables:
a = 1
b = 2
c = True

# This neatly defines a list of conditions for the variables to satisfy:
rules = [a == 1,
         b == 2,
         c == True]

# If all the conditions defined in "rules" are satisfied by the values of the variables, then "Success!":
if all(rules):
    print("Success!")

# This is a really lovely little bit of code that solves some issues related -
# - to stacking "if" and "elif" statements repeatedly.
