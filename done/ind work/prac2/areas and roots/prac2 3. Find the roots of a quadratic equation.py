import math

a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
c=float(input("Enter value of c: "))

D=math.pow(b,2)-4*a*c

if D>0:
    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    print("Quadratic equation has 2 roots:")
    print(x1, x2)
elif D==0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print("Quadratic equation has 1 root:")
    print(x)
else:
    print("Quadratic equation has no roots")
