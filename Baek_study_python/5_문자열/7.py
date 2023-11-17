
n=int(input())

for i in range(n):
    number,alph=input().split()
    number=int(number)
    for j in range (len(alph)):
        print(alph[j]*number,end='')
    
    print()
        