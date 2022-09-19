n = int(input())
a = [ int(input()) for i in range(n)]
print(min(a, key=abs))
print(a[::-1])
#2
a = [85, 22, 1, 5, 99, 29]
b = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
a,b = b,a
print(a)
print(b)
