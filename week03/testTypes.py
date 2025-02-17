i = 3
fl = 3.5
isa = True
memo = 'how now Brown cow'
lots = []


#asked chatgpt if i could stick them all into a loop. the first step was to make a list out of the existing variables.
variables = [i, fl, isa, memo, lots]

#this is my for loop. for every variable in variables, print the type.
for var in variables:
    print(type(var))