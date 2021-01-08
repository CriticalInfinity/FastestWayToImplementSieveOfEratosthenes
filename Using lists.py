import time
n=10**8
start=time.time()
start1=time.time()
prime=[True for x in range(n+1)]
diff=time.time()-start1
print(f"Time Taken To initialize list: {diff} seconds")
h=2
while h*h<=n:
    if prime[h]:
        for i in range(h*h,n+1,h):
            prime[i]=False
    h+=1
stop=time.time()
timetaken=stop-start
print("Time Taken: ",timetaken)