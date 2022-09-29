n = int(input("Enter size: "))
arr = [[int(input("Elements: ")) for j in range(n)] for i in range(n)]
print('\n'.join([''.join([str(f'{i:4}') for i in row]) for row in arr]))
arr = list(zip(*arr))
print('\n'.join([''.join([str(f'{i:4}') for i in row]) for row in arr]))


