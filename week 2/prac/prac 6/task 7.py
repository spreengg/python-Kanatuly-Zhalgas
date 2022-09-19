a = [65, 12, 4, 98, 77, 5, 2]
sum = 0
res = 1 #product of el
for i in range(len(a)):
  if a[i] % 2 != 0:
     res *= a[i]
  else:
      sum += a[i]
print(sum)
print(res)
#2 min max 
a = [0, 22, 53, 49, 56, 763, 1044, 20]
max = a[0]
max_index = 0
min = a[0]
min_index = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
    if a[i] < min:
        min = a[i]
        min_index = i
a[min_index] = max
a[max_index] = min
print(a)
