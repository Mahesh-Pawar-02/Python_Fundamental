import os
import multiprocessing

def Task1(No):
    print("Executing first task")
    print("PID of task1 : ",os.getpid())                                # 51
    print("PPID of task1 : ",os.getppid())                              # 11

def Task2(No):
    print("Executing second task")
    print("PID of task2 : ",os.getpid())                                # 101
    print("PPID of task2 : ",os.getppid())                              # 11
    
def main():
    print("PID of running process : ",os.getpid())                      # 11
    print("PID of parent process ie command prompt is : ",os.getppid()) # 21
    
    Value = 11
    p1 = multiprocessing.Process(target = Task1, args = (Value,))
    p2 = multiprocessing.Process(target = Task2, args = (Value,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

if __name__ == "__main__":
    main()