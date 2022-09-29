import random
N=int(input("Enter n: "))
M=int(input("Enter m: "))
arr=[[random.randrange(10) for i in range(N)] for j in range(M)]
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
print()

for i in arr :
    print(*i)
print()
for row in arr :
    rmin = min(row)
    row = [(1 if rmin % 2 else 0) if j == rmin else j for j in row]
    print(*row)
