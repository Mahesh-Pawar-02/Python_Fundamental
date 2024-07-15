def CheckEven(No):
    if(No % 2 == 0):
        print("It is even number")
    else:
        print("It is odd number")
    
def main():
    print("Enter number : ")
    A = int(input())

    CheckEven(A)

 # Starter   
if __name__ == "__main__":
    main()