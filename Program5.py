def check_odd_or_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
number = int(input("Enter a number: "))

result = check_odd_or_even(number)

# print(f"The number {number} is {result}.")
print("The number {} is {}.".format(number,result))