matrix = []

line = list(map(int, input().split()))

matrix.append(line)

for j in range(len(line) - 1):

   line = list(map(int, input().split()))

   matrix.append(line)

print(matrix)


k = int(input("k: "))

maximum = matrix[0][0]

counter = 0

for arr in matrix:

   for num in arr:

       if num % k == 0:

           if maximum < num:

               maximum = num

           counter += 1

print("{0} numbers, divisible {1}".format(counter, k))

if maximum != 0:

   print("Max num divisible: {0} - {1}".format(k, maximum))

else:

   print("No numbs divisible {0}".format(k))
