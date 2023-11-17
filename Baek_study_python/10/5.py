n=int(input())

a,b=[],[]

for i in range(n):
    c,d=map(int,input().split())
    a.append(c),b.append(d)


h=max(a)-min(a)
w=max(b)-min(b)

print(h*w)