
N, M = map(int, input().split())

arr = []
maxVal = -1
maxI, maxJ = 0, 0

for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(M):
        if row[j] > maxVal:
            maxVal = row[j]
            maxI, maxJ = i, j

print(f"최댓값은 {maxVal}이며, 위치는 ({maxI}, {maxJ})입니다.")



# N, M = map(int, input().split()):

# 사용자로부터 입력을 받습니다.
# input() 함수를 사용하여 사용자로부터 키보드 입력을 받습니다.
# split() 메서드를 사용하여 입력값을 공백을 기준으로 분리합니다.
# map(int, ...) 함수는 분리된 문자열을 정수로 변환합니다.
# N과 M에 각각 변환된 값들을 할당합니다. 이 코드는 N과 M을 입력받는 코드입니다.
# arr = []:

# 비어있는 리스트 arr을 생성합니다. 이 리스트는 나중에 2차원 배열을 저장할 용도로 사용됩니다.
# maxVal = -1:

# maxVal 변수를 -1로 초기화합니다. 이 변수는 최댓값을 추적하는 데 사용됩니다.
# maxI, maxJ = 0, 0:

# maxI와 maxJ 변수를 0으로 초기화합니다. 이 변수들은 최댓값의 위치를 추적하는 데 사용됩니다.
# for i in range(N)::

# for 반복문을 시작합니다. i 변수는 0부터 N-1까지 반복됩니다. 이 반복문은 행을 나타냅니다.
# row = list(map(int, input().split())):

# 사용자로부터 새로운 입력을 받습니다.
# 입력값을 공백을 기준으로 분리하고, 각 부분을 정수로 변환하여 리스트 row에 저장합니다. 이것은 현재 행의 값을 읽어오는 코드입니다.
# arr.append(row):

# row 리스트를 arr 리스트에 추가합니다. 이렇게 하면 2차원 배열을 구성하는 과정입니다.
# for j in range(M)::

# 또 다른 for 반복문을 시작합니다. j 변수는 0부터 M-1까지 반복됩니다. 이 반복문은 열을 나타냅니다.
# if row[j] > maxVal::

# 현재 행 i의 열 j의 값을 최댓값 maxVal과 비교합니다.
# maxVal = row[j]:

# 현재 열의 값이 최댓값보다 크다면, 최댓값 maxVal을 업데이트합니다.
# maxI, maxJ = i, j:

# 최댓값이 업데이트되면, 최댓값의 위치를 maxI와 maxJ 변수에 저장합니다.
# print(f"최댓값은 {maxVal}이며, 위치는 ({maxI}, {maxJ})입니다."):

# 최종적으로 최댓값과 그 위치를 출력합니다. f-string을 사용하여 문자열 안에 변수 값을 삽입합니다.
# 이 코드는 사용자로부터 행과 열의 개수를 입력받고, 그에 따라 2차원 배열을 생성한 후 최댓값과 그 위치를 찾아 출력하는 간단한 예제입니다.




