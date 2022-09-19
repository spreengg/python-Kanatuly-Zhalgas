a = [11, 22, 22, 33, 44, 55, 55]
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] in b:
        print("dublicate:", a[i], i)
    else:
        b.append(a[i])

a = [142, 123, 444, 12, 5, 22, 15, 86]
print(a)
for i in range(8):
    if a[i] < 15:
        a[i] = a[i] * 2
print(a)
