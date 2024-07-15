print("Demonstration of Object Orientation")

######################################################
class Arithematic:
    def __init__(self,Value1, Value2):  # Constructor
        self.No1 = Value1   # Characteristics
        self.No2 = Value2   # Characteristics
    
    def Addition(self):     # Behaviour
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self): # Behaviour
        Ans = self.No1 - self.No2
        return Ans
######################################################

print("Enter first numbner")
A = int(input())

print("Enter second numbner")
B = int(input())

obj = Arithematic(A,B)

Ret = obj.Addition()
print("Addition is : ",Ret)

Ret = obj.Substraction()
print("Substraction is : ",Ret)

