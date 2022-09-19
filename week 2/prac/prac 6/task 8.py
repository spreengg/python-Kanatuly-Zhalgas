a = [11, 222, 12, 56, 44, 245, 76]
sum = 0
res = 1
for i in range(len(a)):
    res *= a[i]
    sum += a[i]
print(sum)
print(res)

a = [48, 34, 74, 0, 55, 11, 0]
sum = 0
for i in a:
    sum += i
mean = sum / len(a)
for i in range(len(a)):
    if a[i] == 0:
        a[i] = mean
print(a)
