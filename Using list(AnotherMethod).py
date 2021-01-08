#This is the fastest method of using Sieve of Eratosthenes
#Mainly this method is approximately 1.06 times faster than the one using numpy arrays

import time
n=10**8
start=time.time()
start1=time.time()
primes=[True]*(n+1)
diff=time.time()-start1
print(f"Time Taken To initialize list: {diff} seconds")
h=2
while h*h<=n:
    if primes[h]:
        for i in range(h*h,n+1,h):
            primes[i]=False
    h+=1
stop=time.time()
timetaken=stop-start
print("Time Taken: ",timetaken)