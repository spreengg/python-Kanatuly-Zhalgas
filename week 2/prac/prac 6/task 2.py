#1st part
a=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   a.append(l)
print(a)

b=min(a)
print("Index of min element: ", a.index(b))

#2nd part
b=[]
for i in range(0, n):
    if a[i]>0:
        b.append(a[i])
print("Postivie numbs: ", b)


c=[]
for i in range(0, n):
    if a[i]<0:
        c.append(a[i])
print("Negative numbs: ", c)
