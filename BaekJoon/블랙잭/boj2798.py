"""
블랙잭
BOJ 2798번 문제
입력 N개 중에서 M을 넘지 않는 최대 숫자 조합 만들기
"""

from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

comb_data = list(combinations(data, 3))

max_val = 0

for comb in comb_data:
    result = 0
    for x in comb:
        result += x
    if result <= m:
        max_val = max(max_val, result)

print(max_val)
