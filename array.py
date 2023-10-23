import numpy as np
def lis():
    l = []
    row = int(input("enter no of row: "))
    col = int(input("enter no of col: "))
    for i in range(row):
        temp = []
        for j in range(col):
            data = int(input(f"enter {i+1} row value {j+1}: "))
            temp.append(data)
        l.append(temp)
    return l

    
z=np.array([lis(),lis()])

p=np.linalg.multi_dot(z)

print(p)


        
        