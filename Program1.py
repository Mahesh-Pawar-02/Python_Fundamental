# Python Program to Calculate the Area of a Triangle

def Triangle_Area(base, height):
    Area = 0.5 * base * height
    return Area

base = float(input("Enter the base of traingle : "))
height = float(input("Enter the height of traingle : "))

Area = Triangle_Area(base, height)
print("The area of the triangle is: ",Area)