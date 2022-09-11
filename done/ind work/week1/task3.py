import math
a=float(input("Enter real num which contain 2 digits before and 2 digits after the coma: "))
b=a//1
c=a%1
b1=b/100  #new dec part
c1=c*100  #new int part
num = c1+b1
print(num)
