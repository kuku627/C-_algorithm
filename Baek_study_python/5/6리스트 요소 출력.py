arr=[-1]*26

alp=list(input())

for i in range(len(alp)):
    if(arr[ord(alp[i])-ord('a')]==-1):
        arr[ord(alp[i])-ord('a')]=i
    
print(*arr)
