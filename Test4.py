def Display(Cnt):
    i = 0   

    if(Cnt <= 0):
        print("Invalid input")
        return
    
    while(i < Cnt):
        print("Jay Ganesh...")  #   end= " "
        i = i + 1

def main():
    Value = int(input("Please enter frequency: "))
    Display(Value)

 # Starter   
if __name__ == "__main__":
    main()