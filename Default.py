def Area(Radius, PI = 3.14):
    Result = PI * Radius * Radius
    return Result

Ans = Area(10.7)
print("Area of circle is : ",Ans)

Ans = Area(10.7, 7.20)
print("Area of circle is : ",Ans)

Ans = Area(Radius=10.7)
print("Area of circle is : ",Ans)