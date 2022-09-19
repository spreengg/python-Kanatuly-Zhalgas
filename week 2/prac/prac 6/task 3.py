n = int(input())
D = [ int(input()) for i in range(n)]
sum = 0
for i in range(1,n,2):
    sum += D[i]
print(D)
print(sum)

a = [45, 122, 14, 9, 342, 11, 60]
print(a)
for i in range(8):
    if a[i] < 15:
        a[i] = a[i] * 2
print(a)



