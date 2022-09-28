import math

def triangleArea(base,height):
    return (height * base) / 2
def rectangleArea(length,width):
    return length * width

a = int(input("long base: "))
b = int(input("short base: "))
h = int(input("height: "))
t = int(input("leg: "))

print("Area:", triangleArea(a-b,h) + rectangleArea(b,h))

