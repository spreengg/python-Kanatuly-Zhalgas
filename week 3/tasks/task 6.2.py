import math

def triangleAreaSemiP(a,b,c):
    s = (a + b + c) / 2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
h = int(input("diagoal (A,C): "))
print(triangleAreaSemiP(a,b,h) + triangleAreaSemiP(c,d,h))


