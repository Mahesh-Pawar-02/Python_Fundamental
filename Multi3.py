
def EvenDisplay(No):
    print("List of even numbers : ")
    x = 2
    for i in range(No):
        print(x)
        x = x + 2

def OddDisplay(No):
    print("List of odd numbers : ")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2
def main():
    print("Enter number : ")
    Value = int(input())

    EvenDisplay(Value)
    OddDisplay(Value)

if __name__ == "__main__":
    main()