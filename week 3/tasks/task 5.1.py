import math

def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

def gcd(x,y):
    if (y == 0):
        return abs(x)
    else:
        return gcd(y, x % y)

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
a /= gcd(a,b)
b /= gcd(a,b)
c /= gcd(c,d)
d /= gcd(c,d)
b2 = lcm(b,d)
d2 = b2
a *= b2 / b
c *= d2 / d
print(a - c, "/", b2)
