text = str(input("Enter text: "))
count = 0
while text.find("a") != -1:
    text = text.replace("a", "o", 1)
    count += 1

print("Text: ",text)
print("Replacements:",count)
print("len of text: ",len(text))
