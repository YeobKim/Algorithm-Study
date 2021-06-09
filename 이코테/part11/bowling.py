"""
볼링공 고르기
permutations를 이용해서 조합을 구한다음 같은 무게인 것만 제외
"""
from itertools import combinations

n, m = map(int, input().split())
ball_w = list(map(int, input().split()))

com = list(combinations(ball_w, 2))
print(com)

for x in com:
    if x[0] == x[1]:
        com.remove(x)

print(len(com))
