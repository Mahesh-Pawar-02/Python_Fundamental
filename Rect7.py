i = 1

def DisplayR(No):
    global i
    if(i <= No):
        print(i)
        i = i + 1
        DisplayR(No)

def main():
    num = int(input("Enter number : "))
    DisplayR(num)
    
if __name__ == "__main__":
    main()