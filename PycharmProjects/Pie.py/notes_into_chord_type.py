# This program takes notes as inputs, and defines triads based on those notes.
# Inputs:
root = 'a'
third = 'c#'
fifth = 'e'

# This section defines a bunch of conditions for each chord.
a_major = [root == 'a',
           third == 'c#',
           fifth == 'e']
a_minor = [root == 'a',
           third == 'c',
           fifth == 'e']

a_sharp_major = [root == 'a#',
           third == 'd',
           fifth == 'f']
a_sharp_minor = [root == 'a#',
           third == 'c#',
           fifth == 'f']

b_major = [root == 'b',
           third == 'd#',
           fifth == 'f#']
b_minor = [root == 'b',
           third == 'd',
           fifth == 'f#']

c_major = [root == 'c',
           third == 'e',
           fifth == 'g']
c_minor = [root == 'c',
           third == 'd#',
           fifth == 'g']

c_sharp_major = [root == 'c#',
           third == 'f',
           fifth == 'g#']
c_sharp_minor = [root == 'c#',
           third == 'e',
           fifth == 'g#']



# This section outputs the chord based on note inputs.
if all(a_major):
    d = 'A-major chord.'



print(d)

