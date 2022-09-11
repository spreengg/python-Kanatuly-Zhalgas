import math

x=int(input("Enter a variable x: "))
y=int(input("Enter a variable y: "))
print()
H=math.sqrt(math.cos(2*y)+math.sin(4*y)+math.sqrt(math.exp(x)+math.exp(-x))) / math.pow((math.exp(-x)+math.exp(x)), 3)*math.pow((math.sin(4*y)+math.cos(2*y)-2),2)
print(H)
