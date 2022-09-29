import random
N=int(input("Enter n: "))
A=[[random.randrange(10) for i in range(N)] for j in range(N)]

for i in A:
    for j in i:
        print(j, end=" ")
    print()
summ = 0
count= 0
for i in range(len(A) - 1):
    for j in range(i + 1, len(A[i])):
        if A[i][j] > 0:
            summ += A[i][j]
            count += 1
print("Sum of positive numbs: ", summ)
print("Count of pos. numbs: ", count)
