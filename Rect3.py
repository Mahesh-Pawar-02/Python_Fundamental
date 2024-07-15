def fun():
    print("Inside fun")
    fun()

def main():
    fun()
    
if __name__ == "__main__":
    main()