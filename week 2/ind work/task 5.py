list = [1,-5,3,-9,25,10]
def absolute_value(num):
    return abs(num)
list.sort(key = absolute_value)
list.reverse()

print("List in descending order: ", list) 

