import sys

def main():
    print("Demonstration of command line agrguments")
    print("Name of application : ",sys.argv[0])

    print("Datatype of argv is : ",type(sys.argv))

    print('Number of command line argument : ',len(sys.argv))

if __name__ == "__main__":
    main()