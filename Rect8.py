i = 1

def DisplayR(No):
    global i
    if(No >= 1):
        print(No)
        No = No - 1
        DisplayR(No)

def main():
    num = int(input("Enter number : "))
    DisplayR(num)
    
if __name__ == "__main__":
    main()