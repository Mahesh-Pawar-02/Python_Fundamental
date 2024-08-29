# Python Program to Generate a Random Number

import random

def Number(length = 6):
    num = ""
    for _ in range(length):
        num = num + str(random.randint(0, 9))
    return num

# Example usage:
num = Number()
print("Random Number is:", num)