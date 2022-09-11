import math

x=0.8
y=0.1
z=4

a=(1-x+math.atan(x-7*y))/(4*x*z-math.pows(math.log10(y),2)) **(1./5.)


print(a)
