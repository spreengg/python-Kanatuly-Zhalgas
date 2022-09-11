a=int(input("Enter value: "))
b=int(input("Enter value: "))
c=int(input("Enter value: "))
print()
if a<b:
    if a<c:
        y=a
    else:
        y=c
else:
    if b<c:
        y=b
    else:
        y=c

print("Min num: ", y)
