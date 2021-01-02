import numpy as np
import time
n=10**8
start=time.time()
start1=time.time()
prime1=np.full(n+1,True)#for filling list faster
prime=list(prime1)
print(time.time()-start1)
del np #Unimporting the package to improve timings
h=2
while h*h<=n:
    if prime[h]:
        for i in range(h*h,n+1,h):
            prime[i]=False
    h+=1
stop=time.time()
timetaken=stop-start
print("Time Taken: ",timetaken)