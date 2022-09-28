import math


def hypotenuses(a,b):
    return math.sqrt(a**2 + b**2)

def isInCircle(r,x,y):
    if r > hypotenuses(x,y):
        return True
    else:
        return False

a = int(input("a: "))
b = int(input("b: "))
r = int(input("r: "))

p1 = int(input("p1: "))
p2 = int(input("p2: "))
print(isInCircle(r,abs(p1) - abs(a),abs(p2) - abs(b)))
f1 = int(input("f1: "))
f2 = int(input("f2: "))
print(isInCircle(r,abs(f1) - abs(a),abs(f2) - abs(b)))
l1 = int(input("l1: "))
l2 = int(input("l2: "))
print(isInCircle(r,abs(l1) - abs(a),abs(l2) - abs(b)))

