# Marvellous.py file import is compulsory
import Marvellous

def main():
    print("Enter first number : ")
    A = int(input())

    print("Enter second number : ")
    B = int(input())

    Ans = Marvellous.Addition(A, B)

    print("Addition is : ",Ans)

    Ans = Marvellous.Multiplication(A, B)
    print("Multiplication is: ",Ans)

main()