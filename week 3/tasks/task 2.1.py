import math
def regTriangleArea(a):
    return (math.sqrt(3) / 4) * a ** 2
a = int(input("Side of regular hexagon: "))
print("Area of regular hexagon is:", regTriangleArea(a)*6)
