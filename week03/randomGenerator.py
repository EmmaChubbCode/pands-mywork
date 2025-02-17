# program that prints out a random number between 1 and 10
#import random

#number = random.randint(1,10)
#print("here is a random number {}".format(number))

# same again but this time use input so the user picks the ranges.
import random

# Get range from user
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

# Generate a random number in the given range
number = random.randint(low, high)

# Print the random number
print(f"Here is a random number: {number}")