import random
N=int(input("Enter n: "))
M=int(input("Enter m: "))
a=[[random.randrange(10) for i in range(N)] for j in range(M)]
for i in a:
    for j in i:
        print(j, end=" ")
    print()
print()
print(list(map(sorted, a)))
def sortarr(a): 
    if len(a) <= 1:
        return a
    else:
        return sortarr( [x for x in a[1:] if x < a[0]]) + [a[0]] + sortarr([x for x in a[1:] if x >= a[0]] )
sortarr(a)
