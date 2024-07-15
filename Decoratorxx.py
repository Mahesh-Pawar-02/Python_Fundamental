# Predefined function

def sub(A, B):
    if A < B:       # avoid written in built function
        A,B = B,A
    print(A-B)


def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    sub(No1, No2)

if __name__ == "__main__":
    main()