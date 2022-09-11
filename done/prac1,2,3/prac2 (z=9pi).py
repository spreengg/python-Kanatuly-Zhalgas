import math

x=int(input('enter variable x: '))
t=int(input('enter variable t: '))
z=((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)- math.fabs(math.sin(t)))) * math.pow(math.e,x)
print("z={0:2f}".format(z))
