import math

print("1) rectangle ")
print("2) circle ")
print("3) triangle ")
a=int(input("Choose your geometric figure: "))

if a==1:
    b=int(input("Enter length of 1st side: "))
    c=int(input("Enter length of 2nd side: "))
    area=b*c
    print("Area of a rectangle is ", area)
elif a==2:
    r=int(input("Enter radius of circle: "))
    area=math.pi*math.pow(r,2)
    print("Area of a circle is ",area)
elif a==3:
    b=int(input("Enter length of 1st side: "))
    c=int(input("Enter length of 2nd side: "))
    d=int(input("Enter length of 3nd side: "))
    s = (a + b + c) / 2 #semip
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("Area of the triangle is", area)
    
    
    
