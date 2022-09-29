N = 3
#A = [[1, 2, 3],[2, 5, 6],[3, 6, 4]]
A = [[1, 2, 3],[2, 5, 6],[3, 3, 1]]
b = "YES"
for i in range(N):
    for j in range(N):
        if A[i][j] != A[j][i]:
            b = "NO"
            break
print(b)

