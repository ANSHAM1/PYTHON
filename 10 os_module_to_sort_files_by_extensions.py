import os
f=os.listdir("data")
png=jpg=txt=0
for i in f:
    a=os.path.splitext(i)
    b=a[1]
    if b=='.png':
        png+=1
        os.rename(f"data/{i}",f"data/{png}")
    elif b=='.jpg':
        jpg+=1
        os.rename(f"data/{i}",f"data/{jpg}")
    elif b=='.txt':
        txt+=1
        os.rename(f"data/{i}",f"data/{txt.txt}")
    else:
        pass
