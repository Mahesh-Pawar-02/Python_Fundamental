# Marvellous.py file import is compulsory
from Marvellous import Addition
from Marvellous import Multiplication

def main():
    print("Enter first number : ")
    A = int(input())

    print("Enter second number : ")
    B = int(input())

    Ans = Addition(A, B)

    print("Addition is : ",Ans)

    Ans = Multiplication(A, B)
    print("Multiplication is: ",Ans)

main()