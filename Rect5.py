
i = 1
def fun():
    global i
    print("Inside fun",i)
    i = i + 1
    fun()

def main():
    fun()
    
if __name__ == "__main__":
    main()