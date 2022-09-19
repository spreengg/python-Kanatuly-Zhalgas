a = [99, 98, 98, 97, 96, 95, 94, 93, 92, 91]
for i in range(len(a)):
    print(a[i],-a[i])

a = [12, 22, 44, 22, 53, 3, 66, 78, 66]
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)
