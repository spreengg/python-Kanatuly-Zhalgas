import math

def countDividers(n):
    if n <= 0: return 0 
    if n == 1: return 1

    k = 2 
    for i in range(2, round(math.sqrt(n)) + 1): 
        if n % i == 0:
            k += 1 if i == n // i else 2
    return k

def maxDividersCountAtRange(m , n):
    if m > n : m, n = n, m 

    maxDivs = 0 
    numberWithMaxDivs = [] 
    for i in range(m, n): 
        d = countDividers(i)
        if d > maxDivs: 
            maxDivs = d
            numberWithMaxDivs = [] 
        if d == maxDivs:
            numberWithMaxDivs.append(i) 

    return maxDivs, numberWithMaxDivs

print(maxDividersCountAtRange(20,80))
