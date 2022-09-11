a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
c=input("Choose operation (+,-,*,/): ")
if c=='+':
    print("Result: ", a+b)
elif c=='-':
    print("Result: ", a-b)
elif c=='*':
    print("Result: ", a*b)
elif c=='/':
    if b==0:
        print("Cannot devide by 0!!!")
    elif b!=0:
        print("Result: ", a/b)
