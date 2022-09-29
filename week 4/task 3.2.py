n=2
m=3
a=[[11, 12, 13],[22, 33, 44]]
for i in a:
    print(i)
    
max=a[0][0]
for i in range(n):
    for j in range(n):
        if max<a[i][j]:
            max=a[i][j]
print()
print ("max = ", max)
print()

for i in range(n-1):
    for j in range(m-1):
        if a[i][j]<a[i+1][j]:
            a[i], a[j] = a[j], a[i]

for j in range(m-1):
    for i in range(n-1):
        if a[i][j]<a[i][j+1]:
            a[i], a[j] = a[j], a[i]

for i in a:
    print(i)

