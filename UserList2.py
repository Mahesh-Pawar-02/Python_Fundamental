def Addition(Data):
    Sum  = 0

    for no in Data:
        Sum = Sum + no
    return Sum

def main():
    print("Enter number of elements : ")
    size = int(input())

    Arr = list()

    print("Enter elements : ")
    for i in range(size):
        no = int(input())

        Arr.append(no)

    print("Enetred elements are: ",Arr)

    Result = Addition(Arr)
    print("Summation of all elements : ", Result)

if __name__ == "__main__":
    main()