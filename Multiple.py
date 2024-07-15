
def Calculations(No1, No2):
    Add = No1 + No2
    Sub = No1 - No2
    return Add, Sub

print("Enter first number : ")
A = int(input())

print("Enter second number : ")
B = int(input())

Result1, Result2 = Calculations(A, B)

print("Addition is: ",Result1)
print("Substraction is: ",Result2)