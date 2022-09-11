import math

a=int(input("Enter length of the 1st leg (in cm): "))
b=int(input("Enter length of the 2nd leg (in cm): "))
c= math.sqrt(math.pow(a,2)+math.pow(b,2))

#perimeter
p=a+b+c
print(p)
print()

#area
area=(a*b)/2
print(area)
print()
