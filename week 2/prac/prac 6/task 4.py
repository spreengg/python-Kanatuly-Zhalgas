n = int(input())
a = [ int(input()) for i in range(n)]
max = a[0]
max_index = 0 #find max
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
print(max_index + 1)

a = [54, 23, 44,98, 83, 31, 41, 57]
b = []
for i in range(len(a)):
    if a[i] % 2 == 1:
        b.append(a[i])

if len(b) == 0:
    print("no such numbers")
else:
    b.sort()
    print(b[::-1]) #des. oreder





