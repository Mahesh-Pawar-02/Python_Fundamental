# Predefined function

def sub(A, B):
    print(A-B)

def SmartSub(fptr):
    def Inner(A,B):
        if A < B :
            A, B = B, A
        return fptr(A, B)
    return Inner

sub = SmartSub(sub)

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    sub(No1, No2)

if __name__ == "__main__":
    main()