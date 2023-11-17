N,X=map(int,input().split())


arr=list(map(int,input().split()))

for i in range(N):
    if(arr[i]<X):
        print(arr[i],end=' ')

print(str(arr))#이건 리스트 출력하기
