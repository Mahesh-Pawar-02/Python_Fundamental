i = 1
Fact = 1

def Factorial(No):
    global i
    global Fact

    if(No >= 1):
        Fact = Fact * No
        No = No - 1
        Factorial(No)

    return Fact

def main():
    num = int(input("Enter number : "))

    Ret = Factorial(num)

    print("Factorial is : ",Ret)
    
if __name__ == "__main__":
    main()