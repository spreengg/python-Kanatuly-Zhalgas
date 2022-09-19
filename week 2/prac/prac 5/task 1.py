Text = str(input("Text: "))
txt = Text.split()
count =0
for words in txt:
    if words[0] == "e" or words[0] =="E":
        count+=1
print(count)
