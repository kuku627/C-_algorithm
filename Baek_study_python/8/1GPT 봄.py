# alpha={}

# for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     alpha[i]=ord(i)-ord('A')+10
#     print(alpha[i])

N,B=input().split()
B=int(B)
# N = [i for i in N]
Number=int(N,B)
# result = str(Number)
print(Number)


# "B = [i for i in N]" 이 구문은 리스트 컴프리헨션(list comprehension)을 사용한 것입니다. 이 구문은 N이라는 리스트(또는 이터러블 객체)의 각 요소를 순회하면서 새로운 리스트 B를 생성합니다.

# 구체적으로 이 구문이 어떻게 동작하는지 설명하면 다음과 같습니다:

# for i in N: 이 부분은 N 리스트의 각 요소를 순회하는 반복문입니다. i는 각 요소를 나타냅니다.

# i for i in N: 각 요소 i를 그대로 가져와서 새로운 리스트에 포함시킵니다. 따라서 B 리스트에는 N 리스트의 요소들이 그대로 복사됩니다.

# 결과적으로, "B = [i for i in N]" 구문은 N 리스트의 모든 요소를 새로운 리스트 B에 복사하는 역할을 합니다. 이 때 B 리스트는 N 리스트와 동일한 요소들을 가지게 됩니다.