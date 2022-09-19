import math

n=int(input("Enter the length  of str: "))
num=math.floor(n/2)
print(num)
a=str(input("Enter text: "))

for i in range(num):
    if a[i]=='n':
        a = a.replace("n", "*")
print("New string:  ", a)
    

    

