def DisplayF():
    print("Inside Display of for loop")
    for i in range(1,6):
        print(i)
    
def DisplayW():
    print("Inside Display of for while")
    no = 1
    while(no <= 5) :
        print(no)
        no = no + 1

def main():
    DisplayF()
    DisplayW()

if __name__ == "__main__":
    main()