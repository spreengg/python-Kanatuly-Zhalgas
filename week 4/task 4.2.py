a = [[1,2,-3],[-1,2,3],[1,-2,3]]
for i in a:
    for j in i:
        print(j, end=" ")
    print()
print()
a = [[1 if x>0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x<=i else '' for x in range(len(a[i]))],'')
