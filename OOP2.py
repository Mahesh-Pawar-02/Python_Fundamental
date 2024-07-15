
class Demo:
    Data1 = 11  # class variable
    Data2 = 21  # class variable

    def __init__(self, A, B):   # instance method
        print("Inside constructor")
        self.No1 = A    # instance variable
        self.No2 = B    # instance variable

    def Display(self):  # instance method
        print("Value of No1 from dipslay : ",self.No1)
        print("Value of No2 from dipslay : ",self.No2)
        print("Value of Data1 from dipslay : ",Demo.Data1)
        print("Value of Data2 from dipslay : ",Demo.Data2)
        
    @classmethod
    def Fun(cls):   # class method
        print("Value of Data1 from Fun : ",Demo.Data1)
        print("Value of Data2 from Fun : ",Demo.Data2)  

    @staticmethod
    def Gun():
        print("Inside static method")

Demo.Fun()
Demo.Gun()
obj = Demo(5,10)
obj.Display()

