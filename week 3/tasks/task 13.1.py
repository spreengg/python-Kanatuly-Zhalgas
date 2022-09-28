num=int(input("please enter number: "))
for num in range(num, 1000):
    sum1=0
    numcp=num
    if(num>=10 and num<100):
        while(num>0):
            digit=int(num%10)
            d2=digit*digit
            sum1=sum1+d2
            num=int(num/10)

    if(num>=100 and num<1000):
        while(num>0):
            digit=int(num%10)
            d2=digit*digit*digit
            sum1=sum1+d2
            num=int(num/10)
    if(numcp==sum1):
        print("angstrong number: ", sum1)
