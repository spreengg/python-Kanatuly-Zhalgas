import numpy as np
N = 10
k = np.random.randint(N)
a = np.random.randint(10, 100, size=(N, N))
print(a)
 
for n in range(0, len(a)):
    print(a[k, n],'/',a[n,n], '=',  a[k,n] / a[n, n])
