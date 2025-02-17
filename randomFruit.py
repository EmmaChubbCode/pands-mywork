import random
fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# we want a random number between 0 and lenght-1. we use -1 because indexing starts at 0 but length goes to 4 (e.g. 4 values).
# So without -1 we could get a value not actually in our list.
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))
