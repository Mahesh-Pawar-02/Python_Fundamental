
# Name = Lambda Parametrs : Logic
# Name(____,______,......)

def CheckEven(A):
    if(A % 2 == 0):
        return True
    else:
        return False

def main():
    Ret = CheckEven(10)
    if Ret == True:
        print("It is even number")
    else: 
        print("It is odd number")

if __name__ == "__main__":
    main()