while True:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break

    arr=[a,b,c]
    arr=sorted(arr)
    a,b,c=arr[0],arr[1],arr[2]
    if a+b<=c:
        print("Invalid")

    else:
        if a==b==/home/sungcheol2/study/baekjoon/10c:
            print("Equilateral")
        elif a==b or b==c or a==c:
            print("Isosceles")
        else:
            print("Scalene")
