n=input("enter a word: ")
l=[]
for i in n:
    l.append(i)
m=l
l.reverse()
if m==l:
    print("it is palindrome")
else:
    print("it is not")
print()


#------------------------------------------------------------


if(n==n[::-1]):
    print("it is pelindrome")
else:
    print("not")


#-----------------------------------------------------------


#r=''.join(reversed(n))

