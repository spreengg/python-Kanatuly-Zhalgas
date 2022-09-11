print("Password requirements: ")
print("1) Length – 8 characters (if less, it is easier to crack, and if longer, it is difficult to remember) ")
print("2) Password must contain uppercase letters, lowercase characters, numbers and specialcharacters ")
print()


def check_pass(pswd):
    errors = {
        "uppercase" : "You need to have at least 1 uppercase character",
        "lowecase" : "You need to have at least 1 lowercase character",
        "num" : "You need to have at least 1 number",
        "sp_char" : "You need to have at least 1 special character",
        "too_long" : "Your password is might be difficult to remember. you should make it shorter",
        "too_short" : "Your password is too short."
    }
    
    capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small="abcdefghijklmnopqrstuvwxyz"
    specialchar="*-#"
    digits="0123456789"
    u, l, n, s = 0, 0, 0, 0

    if len(pswd) > 8:
        return errors["too_long"]
    elif len(pswd) < 8:
        return errors["too_short"]
    else:
        for i in pswd:
            if (i in capital):
                u+=1
            if (i in small):
                l+=1
            if (i in digits):
                n+=1
            if(i in specialchar):
                s+=1

        if u > 0 and l > 0 and n > 0 and s > 0:
            return "The password is perfect"
        else:
            if u==0:
                return errors["uppercase"]
            elif l==0:
                return errors["lowecase"]
            elif n==0:
                return errors["num"]
            else:
                return errors["sp_char"]

print(check_pass("aDASWda#2123"))
    




                
                

        
        
        
        
        
    
    
    

