# Calculate prime numbers

from datetime import datetime
start =  datetime.now()


def prime(n):
    numberOfDiv = 0
    y = 2
    while numberOfDiv < 1 and y < n:
        if n%y == 0:
            numberOfDiv = numberOfDiv + 1
        else:
            y = y + 1
    # return if a prime
    if numberOfDiv == 0 :
        return n
 
primes = []       
for x in range(2, 1000):  
    p = prime(x)
    if p > 1:
        primes.append(p)

print primes

print datetime.now() - start
