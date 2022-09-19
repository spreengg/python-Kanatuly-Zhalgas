text = str(input("Enter text: "))
indexes = []
count = 0
for char in text:
     count+=1
     if char == '"':
        indexes.append(count)
text = text[indexes[0]:indexes[1]-1]
print(text)
