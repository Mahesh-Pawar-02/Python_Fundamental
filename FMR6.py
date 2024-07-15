from functools import reduce

CheckEven = lambda No : (No % 2 == 0)
Increase = lambda No : No + 1
Add = lambda A,B : A+B

# Task : Name of function
# Elements : List of data elements

#   filterX(CheckEven, [11,14,20,23,18,16,15,20])
def filterX(Task, Elements):
    Result = []     # Empty list to store filtered data

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)
            
    return Result

def main():
    Data = [11,14,20,23,18,16,15,20]
    print("Data form input list : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after filter activity : ",FData)

    MData = list(map(Increase, FData))
    print("Data after map activity : ",MData)

    RData = reduce(Add, MData)
    print("Data after reduce activity is : ",RData)

if __name__ == "__main__":
    main()


