import multiprocessing
import os

def Cube(No):
    print("PID is : ",os.getpid())
    return No*No*No

def main():
    Arr = [10,20,30,40]
    Result = []

    P = multiprocessing.Pool()
    Result = P.map(Cube,Arr)
    P.close()
    P.join()

    print(Result)
    
if __name__ == "__main__":
    main()