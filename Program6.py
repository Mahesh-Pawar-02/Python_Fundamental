# Write a Python program to reverse a string.

def reverse(str):
    reversed_str = ''
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage:
String = input("Enter a string: ")
print("Original string:", String)
print("Reversed string:", reverse(String))