# 행렬의 크기 N, M 입력
N, M = map(int, input().split())

# 행렬 A 입력
A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 B 입력
B = [list(map(int, input().split())) for _ in range(N)]

# 두 행렬 덧셈 및 결과 출력
result = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]





# 이 코드는 파이썬을 사용하여 두 개의 행렬을 입력받고, 덧셈 연산을 수행하여 결과를 출력하는 코드입니다. 이 코드에서 사용된 주요 문법 개념을 하나씩 설명하겠습니다:

# 행렬의 크기 입력:

# python
# Copy code
# N, M = map(int, input().split())
# input() 함수는 사용자로부터 키보드 입력을 받는 함수입니다.
# split() 메서드는 문자열을 공백을 기준으로 나누어 리스트로 반환합니다.
# map(int, ...)는 입력된 문자열을 정수로 변환하는 역할을 합니다. 여기서는 입력된 값들을 정수형으로 변환하여 N과 M에 각각 할당합니다.
# 행렬 A 입력:

# python
# Copy code
# A = [list(map(int, input().split())) for _ in range(N)]
# 리스트 컴프리헨션(List Comprehension)을 사용하여 N번 반복하면서 행렬 A의 각 행을 입력받습니다.
# input().split()을 사용하여 한 줄의 숫자들을 입력받고, map(int, ...)를 사용하여 각 숫자를 정수로 변환합니다.
# 이러한 행렬 입력 방식은 여러 줄에 걸쳐 숫자를 입력할 수 있게 합니다.
# 행렬 B 입력:

# python
# Copy code
# B = [list(map(int, input().split())) for _ in range(N)]
# 마찬가지로 리스트 컴프리헨션을 사용하여 행렬 B의 각 행을 입력받습니다.
# 두 행렬 덧셈:

# python
# Copy code
# result = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]
# 리스트 컴프리헨션을 사용하여 두 행렬 A와 B의 각 요소를 같은 위치끼리 더한 결과를 새로운 2차원 리스트 result에 저장합니다.
# for i in range(N)과 for j in range(M)를 사용하여 각 요소에 접근합니다.
# 결과 출력:

# python
# Copy code
# for row in result:
#     print(' '.join(map(str, row)))
# result에 저장된 행렬의 각 행을 순회하면서 출력합니다.
# map(str, row)를 사용하여 각 행의 요소들을 문자열로 변환하고, ' '.join(...)을 사용하여 요소들을 공백으로 구분하여 출력합니다.
# 이렇게 코드는 행렬의 크기 입력, 행렬 A와 B의 입력, 덧셈 연산, 그리고 결과 출력을 수행합니다.




# User
# 파이썬 map 에 대해 알려줘

# ChatGPT
# map() 함수는 파이썬에서 사용되는 내장 함수 중 하나로, 주어진 함수를 시퀀스(리스트, 튜플 등)의 모든 요소에 적용하여 새로운 시퀀스를 생성합니다. map() 함수의 일반적인 구문은 다음과 같습니다:

# python
# Copy code
# map(함수, 시퀀스)
# 함수: 시퀀스의 각 요소에 적용할 함수를 지정합니다.
# 시퀀스: 함수를 적용할 대상 시퀀스(리스트, 튜플 등)를 지정합니다.
# map() 함수는 주어진 함수를 시퀀스의 각 요소에 적용하고 그 결과를 새로운 이터러블(예: 리스트)로 반환합니다. 이 함수는 반복 작업을 간편하게 처리할 때 유용하게 사용됩니다.

# 예를 들어, 주어진 리스트의 모든 요소를 제곱하고 새로운 리스트를 생성하려면 다음과 같이 map() 함수를 사용할 수 있습니다:

# python
# Copy code
# def square(x):
#     return x ** 2

# original_list = [1, 2, 3, 4, 5]
# squared_list = list(map(square, original_list))
# print(squared_list)  # 출력: [1, 4, 9, 16, 25]
# 위 예제에서 map(square, original_list)는 original_list의 각 요소에 square 함수를 적용하여 제곱한 값을 새 리스트로 반환합니다.

# map() 함수는 파이썬 3에서는 이터레이터를 반환하므로, 결과를 리스트 또는 다른 이터러블 타입으로 변환하려면 list() 함수를 사용합니다.























# for row in result:
#     print(' '.join(map(str, row)))
# 이 코드는 파이썬을 사용하여 두 개의 행렬을 입력받고, 덧셈 연산을 수행하여 결과를 출력하는 코드입니다. 이 코드에서 사용된 주요 문법 개념을 하나씩 설명하겠습니다:

# 행렬의 크기 입력:

# python
# Copy code
# N, M = map(int, input().split())
# input() 함수는 사용자로부터 키보드 입력을 받는 함수입니다.
# split() 메서드는 문자열을 공백을 기준으로 나누어 리스트로 반환합니다.
# map(int, ...)는 입력된 문자열을 정수로 변환하는 역할을 합니다. 여기서는 입력된 값들을 정수형으로 변환하여 N과 M에 각각 할당합니다.
# 행렬 A 입력:

# python
# Copy code
# A = [list(map(int, input().split())) for _ in range(N)]
# 리스트 컴프리헨션(List Comprehension)을 사용하여 N번 반복하면서 행렬 A의 각 행을 입력받습니다.
# input().split()을 사용하여 한 줄의 숫자들을 입력받고, map(int, ...)를 사용하여 각 숫자를 정수로 변환합니다.
# 이러한 행렬 입력 방식은 여러 줄에 걸쳐 숫자를 입력할 수 있게 합니다.
# 행렬 B 입력:

# python
# Copy code
# B = [list(map(int, input().split())) for _ in range(N)]
# 마찬가지로 리스트 컴프리헨션을 사용하여 행렬 B의 각 행을 입력받습니다.
# 두 행렬 덧셈:

# python
# Copy code
# result = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]
# 리스트 컴프리헨션을 사용하여 두 행렬 A와 B의 각 요소를 같은 위치끼리 더한 결과를 새로운 2차원 리스트 result에 저장합니다.
# for i in range(N)과 for j in range(M)를 사용하여 각 요소에 접근합니다.
# 결과 출력:

# python
# Copy code
# for row in result:
#     print(' '.join(map(str, row)))
# result에 저장된 행렬의 각 행을 순회하면서 출력합니다.
# map(str, row)를 사용하여 각 행의 요소들을 문자열로 변환하고, ' '.join(...)을 사용하여 요소들을 공백으로 구분하여 출력합니다.
# 이렇게 코드는 행렬의 크기 입력, 행렬 A와 B의 입력, 덧셈 연산, 그리고 결과 출력을 수행합니다.