
# Name = Lambda Parametrs : Logic
# Name(____,______,......)

def CheckEven(A):
    return (A%2 == 0)
    
CheckEvenX = lambda A : (A%2 == 0)

def main():
    Ret = CheckEvenX(10)
    if Ret == True:
        print("It is even number")
    else: 
        print("It is odd number")

if __name__ == "__main__":
    main()