"""
볼링공 고르기
permutations를 이용해서 조합을 구한다음 같은 무게인 것만 제외
"""
from itertools import permutations

n, m = map(int, input().split())
ball_w = list(map(int, input().split()))

per = list(permutations(ball_w, 2))
print(per)

for x in per:
    if x[0] == x[1]:
        per.remove(x)

print(len(per)//2)
