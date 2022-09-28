import random
import math
def prdArr(n):
    prd = 1
    for i in n:
        prd *= i
    return prd
def sumArr(n):
    sum = 0
    for i in n:
        sum += i
    return sum

def meanArr(n,sum):
    return sum/len(n)

for i in range(3):
    a = random.sample(range(100), 15)
    print(a)
    print(prdArr(a))
    print(meanArr(a,sumArr(a)))
