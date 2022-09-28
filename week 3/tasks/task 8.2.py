def swapFirstLast(a):
    a[0],a[len(a)-1] = a[len(a)-1],a[0]
    return a

m = int(input("length of array: "))
A = []
for i in range(m):
    n = int(input("element of array: "))
    A.append(n)

print(A)
print(swapFirstLast(A))
