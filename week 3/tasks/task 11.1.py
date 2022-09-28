def isPrime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

n = int(input("n: "))

for i in range(n,2*n):
    if isPrime(i) and isPrime(i+2):
        print(i,i+2)
