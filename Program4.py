# Write a Python Program to Check if a Number is Positive, Negative or Zero.

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage:
number = int(input("Enter a number: "))

result = check_number(number)
print(f"The number {number} is {result}.")