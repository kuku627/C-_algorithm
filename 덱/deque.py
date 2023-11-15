from collections import deque

# 덱 생성
my_deque = deque()

# 덱의 오른쪽과 왼쪽에 데이터 추가
my_deque.append(1)
my_deque.append(2)
my_deque.appendleft(3)

# 덱의 오른쪽과 왼쪽에서 데이터 제거
item1 = my_deque.pop()
item2 = my_deque.popleft()

print("덱에서 제거된 데이터:", item1, item2)

