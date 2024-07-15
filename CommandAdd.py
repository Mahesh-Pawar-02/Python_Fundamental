import sys

def main():

    print("Demonstration of command line agrguments")

    print("Addition of two numbers : ",int(sys.argv[1])+int(sys.argv[2]))


if __name__ == "__main__":
    main()