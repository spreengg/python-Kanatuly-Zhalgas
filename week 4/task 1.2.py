import random
N = int(input("Enter size1: "))
M = int(input("Enter size2: "))
B = [[random.randrange(10) for i in range(N)] for j in range(N)]
for i in B:
    for j in i:
        print(j, end=" ")
    print()
for x in range(len(B)) :
    idx = B[x].index(min(B[x]))
    B[x][idx], B[x][0] = B[x][0], B[x][idx]
    idx = B[x].index(max(B[x]))
    B[x][idx], B[x][-1] = B[x][-1], B[x][idx]
print(B)
