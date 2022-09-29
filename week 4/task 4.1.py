import random
arr = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
s=[]
for i in range(len(arr)):
    s.append(sum(arr[i]))

print("Largest sum row: ",arr[s.index(max(s))])
print("Sum of elements: ",max(s))
print("Smallest sum row: ",arr[s.index(min(s))])
print("Sum of elements: ",min(s))
