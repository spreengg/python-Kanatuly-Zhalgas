import math
def gcd(x,y):
    if (y == 0):
        return abs(x)
    else:
        return gcd(y, x % y)

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
print(math.trunc(a*d / gcd(a*d,b*c)), "/", math.trunc(b*c / gcd(a*d,b*c)))
