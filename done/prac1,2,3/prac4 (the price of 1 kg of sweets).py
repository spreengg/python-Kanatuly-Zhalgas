import math

n=int(input("Enter the price of 1 kg of sweets: "))
s=n
for i in range(1,10):
    s=n*i
    print("Cost for",i,"kilos: ", s)
    

