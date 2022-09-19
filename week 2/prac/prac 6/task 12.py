n = int(input())
a = [ int(input()) for i in range(n)]
mn = 99999
for i in range(len(a)):
    if a[i] % 2 == 1 and a[i] < mn:
        mn = a[i]
print(mn)

a = [23, 15, 53, 67, 97, 324, 16, 24, 96, 1]
b = [10,9,8,7,6,5,4,3,2,1]
print(a)
print(b)
a,b = b,a
print(a)
print(b)
