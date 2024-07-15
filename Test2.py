def Display(Cnt):
    i = 0   

    if(Cnt <= 0):
        print("Invalid input")
        return
    
    for i in range(Cnt):
        print("Jay Ganesh...")

def main():
    Value = int(input("Please enter frequency: "))
    Display(Value)

 # Starter   
if __name__ == "__main__":
    main()