A,B=map(int,input().split())

C=B-45

if(C<0):
    A=A-1
    B=(60+C)%60
else:
    B=C
if(A<0):
    A+=24

print(A,B)
