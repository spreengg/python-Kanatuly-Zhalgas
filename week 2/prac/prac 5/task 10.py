text = str(input("Enter text: "))
words = text.split()
temp=list()
for word in words:
    temp = list(word)
    temp[0] = temp[0].upper()
print("".join(temp))
