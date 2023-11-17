N=int(input())
sum,i=0,0
while True:
    i,sum=i+1,sum+i
    if sum>=N: break
cnt=N-sum+i-1
i+=1

# print(cnt)
#k짝수라인 a+b- -->///  k 홀수라인 <--
if i%2==0:
    a,b=i-1,1
    for i in range(cnt):
        a,b=a-1,b+1     
else:
    a,b=1,i-1
    for i in range(cnt):
        a,b=a+1,b-1
print(f'{a}/{b}')
