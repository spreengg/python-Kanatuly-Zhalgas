a = [11, 12, 12, 11, 14, 55, 66, 44]
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] in b:
        print("dublicate:", a[i], i)
    else:
        b.append(a[i])

a = [42, 22, 56, 33, 25, 96]
b = []
for i in range(len(a)):
    if a[i] % 2 == 1:
        b.append(a[i])

if len(b) == 0:
    print("no such numbers")
else:
    b.sort()
    print(b[::-1])
