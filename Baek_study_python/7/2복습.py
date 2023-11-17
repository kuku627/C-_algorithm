
A=[]
for i in range(9):
    A.append(list(map(int,input().split())))


M=max(max(row) for row in A)

for i in range(len(A)): # 2차원 배열에서 len하면 행의 개수나옴
    if M==max(A[i]):
        row=i
        column=A[i].index(max(A[i]))

# for i, row in enumerate(A):  # enumerate 사용
#     if M in row:  # M이 row에 있다면
#         max_row = i
#         max_col = row.index(M)
print(M)

print(f'{row+1} {column+1}')