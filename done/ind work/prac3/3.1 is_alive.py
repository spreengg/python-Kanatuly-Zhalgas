health=int(input("Enter your character's hp: "))
def is_alive(health):
    if health<0 or health==0:
        return False
    else:
        return True


print(is_alive(health))
