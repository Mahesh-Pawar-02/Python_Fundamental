# Write a python program to print even length words in a string

def print_even_length_words(String):
    words = String.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)

String = "Shital Mahesh Pawar"

print("Original string:", String)
print("Even length words:")

print_even_length_words(String)