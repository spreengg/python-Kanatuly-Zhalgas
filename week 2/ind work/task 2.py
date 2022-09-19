List = [12, 35, 9, 56, 24]
print("Current list: ", List)
def change(List):
    size = len(List)
     
    temp = List[0]
    List[0] = List[size - 1]
    List[size - 1] = temp
     
    return List
     

print("New list:     ",change(List))
