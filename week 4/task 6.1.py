import random
n=int(input("Enter n: "))
a=[[random.randrange(10) for i in range(n)] for j in range(n)]
for row in a:
    print(*map('{:>3d}'.format, row))
imax = jmax = 0
rmax = []
cmin = a[0].copy()
amax = a[0][0]
for i in range(n):
    if a[i][i] > amax:
        imax = i
        jmax = i 
        amax = a[i][i]
    if a[i][n-i-1] > amax:
        imax = i 
        jmax = n-i-1
        amax = a[i][n-i-1]
    tmax = a[i][0]
    for j in range(n):
        if tmax < a[i][j] :
            tmax = a[i][j]
        if cmin[j] > a[i][j]:
            cmin[j] = a[i][j]
    rmax.append(tmax)            
        
a[n//2][n//2], a[imax][jmax] = a[imax][jmax], a[n//2][n//2]
print('Max in rows:')
print(*rmax)
print('Min in columns:')
print(*cmin)
print()


