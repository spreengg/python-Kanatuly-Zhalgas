import random
N=int(input("Enter n: "))
M=int(input("Enter m: "))
matrix=[[random.randrange(1000) for i in range(N)] for j in range(M)]
for row in matrix:
    rowStr = ''
    for elem in row:
        rowStr += (str(elem) + '   ')
    print(rowStr)
    print('\n')


maxRowSum   = 0
maxRowN     = -1

rowN = 0
for row in (matrix):
    rowSum = 0
    
    for elem in row:
        rowSum += elem

    if maxRowN < rowSum:
        maxRowSum = rowSum
        maxRowN = rowN

    print(' Sum of rows: ' + str(rowN) + ' equal: ' + str(rowSum))
    rowN += 1


print(' Max sum: ' + str(maxRowSum) + ' row: ' + str(maxRowN))
