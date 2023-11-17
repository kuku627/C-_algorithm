from sympy import solve,Eq,symbols

a,b,c,d,e,f=map(int,input().split())


x,y=symbols('x y')

eq1=Eq(a*x+b*y,c)
eq2=Eq(d*x+e*y,f)
ans=solve((eq1,eq2))

print(f'{ans[x]} {ans[y]}')







from sympy import symbols, Eq, solve

# 변수 정의
x, y = symbols('x y')

# 주어진 방정식
eq1 = Eq(3*x - 2*y, 7)
eq2 = Eq(5*x + 4*y, 29)

# 연립방정식 풀기
solution = solve((eq1, eq2), (x, y))

# 결과 출력
print(solution[x], solution[y])




from sympy import symbols, Eq, solve

# 변수 정의
x, y, z = symbols('x y z')

# 주어진 방정식
eq1 = Eq(x + 2*y - z, 7)
eq2 = Eq(2*x - y + 3*z, 4)
eq3 = Eq(3*x + y - 2*z, 12)

# 연립방정식 풀기
solution = solve((eq1, eq2, eq3), (x, y, z))

# 결과 출력
print(solution[x], solution[y], solution[z])