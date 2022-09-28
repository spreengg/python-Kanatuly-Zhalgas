#1
def area(num):

  if num == 1:
    l = int(input("Enter rectangle's length: "))
    b = int(input("Enter rectangle's breadth: "))
    rect_area = l * b
    print(f"The area of rectangle is :", rect_area)
   
  elif num == 2:
    s = int(input("Enter square's side length: "))
    sqt_area = s * s
    print(f"The area of square is: ", sqt_area)
 
  elif num == 3:
    h = int(input("Enter triangle's height length: "))
    b = int(input("Enter triangle's breadth length: "))
    tri_area = 0.5 * b * h
    print(f"The area of triangle is: ", tri_area)
 
  elif num == 4:
    r = int(input("Enter circle's radius length: "))
    pi = 3.14
    circ_area = pi * r * r
    print(f"The area of circle is: ", circ_area)
     
  else:
    print("You entered wrong num! ")

print("rectangle - 1; square - 2; triangle - 3; circle - 4")
num=int(input("Pick a shape: "))
area(num) 


