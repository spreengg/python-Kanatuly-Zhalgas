import math

def hypotenuses(a,b):
    return math.sqrt(a**2 + b**2)

temp = []
for i in range(2):
        a = int(input("a: "))
        b = int(input("b: "))
        print("hypotenuses of triangle is:",hypotenuses(a,b))
        temp.append(hypotenuses(a,b))

if temp[0] > temp [1]:
    print("hypotrnuses of first triangle is bigger")
elif temp[1] > temp[0]:
    print("hypotrnuses of second triangle is bigger")
else:
    print("hypotrnuses of both triangles are same")

