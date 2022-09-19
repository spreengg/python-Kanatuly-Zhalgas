Text = str(input("Enter text:  "))
count = 0
while Text.find("t") != -1:
    Text = Text.replace("t", "", 1)
    count += 1
print("Number of letter 't': ",count)
