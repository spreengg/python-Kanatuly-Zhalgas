def sumOFAllDivisors(n):
    ans = 0
    for i in range(1,n+1):
        if n % i == 0:
            ans+= i
    return ans

n = int(input("N: "))
for i in range(n):
    a = sumOFAllDivisors(i)
    for j in range (i+1,n):
        b = sumOFAllDivisors(j)
        if a == b:
            print(i,j)
            continue
