import numpy as np
import time
n=10**8
start=time.time()
start1=time.time()
arr=np.full(n+1,True)#for filling list faster
primes=arr.tolist()
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