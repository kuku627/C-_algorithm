from collections import deque

# 덱 생성
rotating_queue_before = deque([1, 2, 3, 4, 5])
print("회전 전 덱의 상태", rotating_queue_before)
# 큐 회전 (오른쪽으로 2칸 이동)
rotating_queue_before.rotate(2)
print("회전 후 덱의 상태:", rotating_queue_before)

