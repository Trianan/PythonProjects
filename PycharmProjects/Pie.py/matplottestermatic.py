# matplotlib with function mod by Tristin Manson (link from source for matplotlib code printed in cmd) 9/14/2020
# importing the required module
import math

import matplotlib.pyplot as plt

# This section is written by Tristin Manson:

# F(x) = sin(x), I think I made it work?
n_squared_list = []
n_plus_list = []
n = 0 #For some reason this has to be zero?
while n < 101:
    n_squared = math.sin(n)
    n_squared_list.append(n_squared)
    n = n+1

# 0-100 x-value list generator:
n = 0
while n < 101:
    n_plus = n+1
    n_plus_list.append(n_plus)
    n = n+1

# Plug values created from function into matplotlib's x,y values:
# x axis values
x = n_plus_list
# corresponding y axis values
y = n_squared_list

# END OF MODIFICATIONS.

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph (And displaying helpful link)
plt.title('F(x) = sin(x)')

# Another mod:
import sys
sys.stdout.write("https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/")
# END OF MODIFICATIONS.

# function to show the plot
plt.show()


