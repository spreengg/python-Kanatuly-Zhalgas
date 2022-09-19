text = str(input("Enter text "))
count = 0
while text.find(".") != -1:
    text = text.replace(".", "", 1)
    count += 1
print(count)
print(text)
