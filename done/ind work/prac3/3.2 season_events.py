bornmonth=int(input("Enter number of month in which you was born (1-12): "))
def season_events(bornmonth):
    if bornmonth==12 or bornmonth==1 or bornmonth==2:
        print("White snow fell outside the window")
    elif bornmonth==3 or bornmonth==4 or bornmonth==5:
        print("Birds sang beautiful songs")
    elif bornmonth==6 or bornmonth==7 or bornmonth==8:
        print("The sun shone brighter than ever")
    elif bornmonth==9 or bornmonth==10 or bornmonth==11:
        print("The harvest was incredible")
    else:
        print("You entered wrong number!")

print()
season_events(bornmonth)
