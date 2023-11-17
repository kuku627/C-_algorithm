N,M=map(int,input().split())
arr=[]
for i in range(N+1):
    arr.append(i)



for i in range(M):
    a,b=map(int,input().split())
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp


for i in range(1,N+1):
    print(arr[i],end=' ')

# 더 좋은 방식
# N, M = map(int, input().split())
# arr = list(range(N + 1))

# for _ in range(M):
#     a, b = map(int, input().split())
#     arr[a], arr[b] = arr[b], arr[a]  # 변수의 값을 교환

# for i in range(1, N + 1):
#     print(arr[i], end=' ')
