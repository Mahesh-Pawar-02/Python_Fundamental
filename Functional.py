print("Demonstration of Functional")

Addition = lambda No1, No2 : No1 + No2

Substraction = lambda No1, No2 : No1 - No2

print("Enter first numbner")
A = int(input())

print("Enter second numbner")
B = int(input())

Ret = Addition(A,B)
print("Addition is : ",Ret)

Ret = Substraction(A,B)
print("Substraction is : ",Ret)
