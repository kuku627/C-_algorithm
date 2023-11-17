import statistics
arr=[]
for i in range(5):
    k=int(input())
    arr.append(k)

arr.sort()
print(statistics.mean(arr))#평균
print(statistics.median(arr))#중앙값

