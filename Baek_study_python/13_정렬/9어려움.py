N = int(input())  # 단어의 개수

words = set()  # 중복을 제거한 단어를 저장할 집합(set)

# 단어 입력 및 중복 제거
for _ in range(N):
    word = input().strip()
    words.add(word)

# 중복을 제거한 단어들을 리스트로 변환하여 정렬
sorted_words = sorted(list(words), key=lambda x: (len(x), x))

# 결과 출력
for word in sorted_words:
    print(word)
