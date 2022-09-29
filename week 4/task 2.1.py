A = [[4, 3, 3], [3, 4, 3], [3, 3, 4]]
B = [[2, 7, 6], [9, 5, 1], [4, 3, 1]]

def ismagic(matrix):
    summ = sum(matrix[0])
    for i in range(len(matrix)):
        temp = 0
        for j in range(len(matrix)):
            temp += matrix[j][i]
        if temp != summ or sum(matrix[i]) != summ:
            return False
    return True
 
print(ismagic(A))
print(ismagic(B))
