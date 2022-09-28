def Palindrome(n: int) -> bool:
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return (n == rev)
def count(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if Palindrome(i):
            print(i, end = " ")
if name == "main":
    count(1, 1000)
