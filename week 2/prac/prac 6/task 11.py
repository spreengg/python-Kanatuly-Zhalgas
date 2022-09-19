n = int(input())
a = [ int(input()) for i in range(n)]
max = 1
for i in range(len(a)):
    if a[i] > max and a[i] % 2 == 0:
        max = a[i]
print(max)

n = int(input())
a = [ int(input()) for i in range(n)]
b = []
for i in range(len(a)):
    if a[i] < 10 and a[i] % 2 == 0:
        b.append(a[i])
    if i == len(a) - 1 and len(b) == 0:
        print("no such numbers")
b.sort()
print(b)
