import multiprocessing
import os
import time

def Fun(No):
    Sum = 0
    print("PID is : ",os.getpid())
    for i in range(No):
        Sum = Sum + (No*No*No)
    return Sum

def main():
    starttime = time.time()
    Arr = [10000,20000,30000,40000,50000]
    Result = []

    P = multiprocessing.Pool()
    Result = P.map(Fun,Arr)
    P.close()
    P.join()

    print(Result)
    endtime = time.time()
    print("Time requred for execution : ",endtime-starttime)
    
if __name__ == "__main__":
    main()