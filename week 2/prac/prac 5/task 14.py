Text = str(input("Enter text: "))
words = Text.split()
for word in words:
    if word[len(word)-1] == "i":
        print(word)
    elif word[0]=="a":
        print(word)
   
            

