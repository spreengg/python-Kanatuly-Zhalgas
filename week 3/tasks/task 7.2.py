def decToOct(n):
    return '{:010o}'.format(n)

a = int(input("Enter num: "))
print(decToOct(a))
