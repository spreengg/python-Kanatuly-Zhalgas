a=[11,22,33,44,55,66,77,88]
b=[1,2,3,4,5,6,7,8]
c=[12,23,34,45,56,67,78,89]
Sum=0
mean=0
def ss(arr):
    global Sum
    global mean
    for i in range(len(arr)):
        Sum = Sum + arr[i]
    mean= Sum/len(arr)
    print("Sum of array:",Sum)
    print("Mean of array:",mean)
    print()

a1=ss(a)
b1=ss(b)

c1=ss(c)


    

