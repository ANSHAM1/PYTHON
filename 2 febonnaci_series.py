import functools

@functools.lru_cache(maxsize=None)
def febo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return febo(n-1)+febo(n-2)

x=int(input("enter a no: "))
for i in range(x):
    print(febo(i),end=',')