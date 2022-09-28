def sumOfDigits(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

n = int(input("N: "))
sub = sumOfDigits(n)
ans = 0
while n > 0:
    ans += 1
    n -= sub

print(ans)
