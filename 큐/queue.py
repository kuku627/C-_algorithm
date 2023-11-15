import queue

# 큐 생성
my_queue = queue.Queue()

# 큐에 데이터 추가
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

# 큐에서 데이터 가져오기
while not my_queue.empty():
    item = my_queue.get()
    print("큐에서 꺼낸 데이터:", item)

# 출력 결과:
# 큐에서 꺼낸 데이터: 1
# 큐에서 꺼낸 데이터: 2
# 큐에서 꺼낸 데이터: 3

