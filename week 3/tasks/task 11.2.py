def findMax(arr, n):
    max = -1
    x = 0
    y = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max:
                max = arr[i][j]
                x = i
                y = j
    return x,y

arr1 = np.random.randint(100, size=(4, 4))
arr2 = np.random.randint(100, size=(4, 4))
print(arr1)
print(arr2)

max1 = findMax(arr1,4)
max2 = findMax(arr2,4)

arr1[max1[0]][max1[1]],arr2[max2[0]][max2[1]] =  arr2[max2[0]][max2[1]],arr1[max1[0]][max1[1]]
print(arr1)
print(arr2)
