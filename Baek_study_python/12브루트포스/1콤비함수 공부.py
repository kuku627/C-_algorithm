from itertools import combinations



N,M=map(int,input().split())
card=list(map(int,input().split()))

for comb in combinations(card, 3):
    print(f'{comb}, {sum(comb)}')
    # 조합과  그 조합의 합


