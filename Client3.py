# Marvellous.py file import is compulsory
import Marvellous as M  #alies

def main():
    print("Enter first number : ")
    A = int(input())

    print("Enter second number : ")
    B = int(input())

    Ans = M.Addition(A, B)

    print("Addition is : ",Ans)

    Ans = M.Multiplication(A, B)
    print("Multiplication is: ",Ans)

main()