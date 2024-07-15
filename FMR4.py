from functools import reduce

CheckEven = lambda No : (No % 2 == 0)

Increase = lambda No : No + 1

Add = lambda A,B : A+B

def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    iCnt = 0
    for iCnt in range(0,Size):
        No = int(input())
        Data.append(No)
        
    print("Data form input list : ",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after filter activity : ",FData)

    MData = list(map(Increase, FData))
    print("Data after map activity : ",MData)

    RData = reduce(Add, MData)
    print("Data after reduce activity is : ",RData)

if __name__ == "__main__":
    main()


