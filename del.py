a=input(" enter no separated by spaces")
z=list(map(int,a.split(" ")))
n=list(map(lambda x:"true" if x%2==0 else "false",z))
print(n)