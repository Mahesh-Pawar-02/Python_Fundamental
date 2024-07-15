
def main():
    print("Enter number of elements : ")
    size = int(input())

    Arr = list()

    print("Enter elements : ")
    for i in range(size):
        no = int(input())

        Arr.append(no)

    print("Enetred elements are: ",Arr)

if __name__ == "__main__":
    main()