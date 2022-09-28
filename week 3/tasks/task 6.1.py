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
    
a = int(input("a: "))
b = int(input("b: "))

print("gcd of a and b:",gcd(a,b))
print("lcm of a and b:",lcm(a,b))
