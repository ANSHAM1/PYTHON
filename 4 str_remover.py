s=input("enter a string")
n=int(input("enter no of places to remove"))
def str_remo(s,n):
    l=list(s)
    l.reverse()
    for i in range(0,n):
        l.pop()
    l.reverse()
    for j in l:
        print(f"{j}",end="")

str_remo(s,n)