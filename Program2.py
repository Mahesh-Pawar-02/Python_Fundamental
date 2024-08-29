# Python Program to Swap Two Variables

def swap(No1, No2):
    temp = No1
    No1 = No2
    No2 = temp
    return No1, No2

No1 = 5
No2 = 10

print("Before swapping: No1 =", No1, ", No2 =", No2)
No1, No2 = swap(No1, No2)
print("After swapping: No1 =", No1, ", No2 =", No2)