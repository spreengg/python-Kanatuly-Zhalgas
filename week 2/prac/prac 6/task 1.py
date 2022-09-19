import statistics
n=int(input("Enter the length of an array: "))
x=[]
print("Enter the elements of arr 1by1: ")
x=[int(input()) for i in range(n) ]

def max_el(arr,n):
   
   mx = arr[0]               
   for i in range(1, n):         
     if arr[i] > mx:         
         mx = arr[i]  
          
   return mx

avg= statistics.mean(x)

for i in range(n):
   if x[i]==0:
      x[i]==avg


   

x.reverse()
print("Largest element: ",max_el(x,n))
print("Reverse list: ", x)



