# A = [[0 for j in range(100)] for i in range(100)]

A=[0 for i in range(100)]
print(A)






N=int(input())
A=[]
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    A.append(row)