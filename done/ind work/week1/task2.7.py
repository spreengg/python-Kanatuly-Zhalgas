word = str(input("Enter the word: "))
number = int(input("Enter the number: "))
print()
def func(letter,number):
    print(letter * number)
word = tuple(word)
for letters in word:
    func(letters , number)
