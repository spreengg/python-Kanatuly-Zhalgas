a = [11, 2, 1, 44, 24, 2]
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] in b:
        print("dublicate:", a[i])
    else:
        b.append(a[i])
    if(i == len(a) - 1 and len(b) == len(a)):
        print("no dublicates")
print(b)

arr = [1,2,3,4,5,60,50,40,30,20,10]
print(arr)
print([0 if i < 10 else 1 if i > 20 else i for i in arr])
