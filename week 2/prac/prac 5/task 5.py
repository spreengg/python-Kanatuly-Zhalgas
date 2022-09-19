text = str(input("Enter text: "))
for letters in text:
     if ord(letters) >64 and ord(letters)<91:
         text = text.replace(letters,chr(ord(letters)+32))
print(text)
