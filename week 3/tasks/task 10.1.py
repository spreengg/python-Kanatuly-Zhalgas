def digitsOfN(n):
    ans = []
    s = str(n)
    for i in s:
        ans.append(int(i))
    return ans

N = int(input("N: "))
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

ans = []
for i in range(100,N):
    dgts = digitsOfN(i)
    if a in dgts:
        dgts.remove(a)
    if b in dgts:
        dgts.remove(b)
    if c in dgts:
        dgts.remove(c)
    if len(dgts) == 0:
        ans.append(i)
print(ans)
