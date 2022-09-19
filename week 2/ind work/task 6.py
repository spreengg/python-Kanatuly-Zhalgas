
arr=["Hello", "EEEE", "fin", "ok", "a"]
def all_eq(list):
    list2= sorted(list, key=len)
    print(list2) #sort arr to find max lens
    max_len=len(list2[-1])
    print(max_len) #find max length

    for i in range(0, len(arr)):
        if len(arr[i])<max_len:
            j=0
            while j!= max_len:
                arr[j].insert('_')
                j+=1
            
        print(list)
    
 

all_eq(arr)
    
