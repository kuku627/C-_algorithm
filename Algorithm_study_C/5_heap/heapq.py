import heapq

# 리스트를 힙으로 변환
my_heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(my_heap)
print("최소 힙으로 변환된 리스트:", my_heap)

# 최소값 추출
min_value = heapq.heappop(my_heap)
print("최소값:", min_value)

# 요소 추가
heapq.heappush(my_heap, 7)
print("요소 추가 후 최소 힙:", my_heap)

