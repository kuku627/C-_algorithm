def k(a1,a0,c,n0):
    for i in range(n0,101):
        if a1*i+a0>c*i:
            return 0
            
    return 1

a1,a0=map(int,input().split())
c=int(input())
n0=int(input())
# 함수 f(n) = a1n + a0, 양의 정수 c, n0가 주어질 경우 
# O(n) 정의를 만족하는지 알아보자.
# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 
# f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}


print(k(a1,a0,c,n0))