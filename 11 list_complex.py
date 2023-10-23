n=[i for i in range(-1,3)]
l=[]
for i in n:
    for j in n:
        for k in n:
            a=i+j+k
            if a==0:
                l.append([i,j,k])
             
count=0
b=[]
for i in l:
    for j in l:
        if i==j:
            continue
        elif j==[0,0,0]:
            continue
        else:
            for k in i:
                for m in j:
                    if m==k:
                        count+=1                
            if count>2:
                b.append(j)
                l.remove(j)
                pass
            count=0

print("triplets: ",l)


