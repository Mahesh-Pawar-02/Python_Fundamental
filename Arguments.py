# Types of function arguments

# 1 : Positional arguments
# 2 : kwyword arguments
# 3 : Default arguments
# 4 : Variable number of arguments

def Information(Name, Age, salary):
    print("Name is : ",Name)
    print("Ag is : ",Age)
    print("salary is: ",salary)

Information("Amit",32,90000)
Information("Pooja",29,70000)

Information(Age=31, salary=78000,Name="Sagar")