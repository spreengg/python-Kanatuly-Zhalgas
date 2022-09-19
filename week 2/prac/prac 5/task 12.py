text = str(input("Enter text: "))
words = text.split()
temp=list()
for word in words:
     temp = list(word)
     if temp[len(temp)-1] == "I":
             print(word)
