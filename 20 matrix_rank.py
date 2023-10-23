import numpy as np

l = []
row = int(input("enter no of row: "))
col = int(input("enter no of col: "))
for i in range(row):
    temp = []
    for j in range(col):
        data = int(input(f"enter {i+1} row value {j+1}: "))
        temp.append(data)
    l.append(temp)

my_matrix = np.array(l)
rank = np.linalg.matrix_rank(my_matrix)

print(rank)