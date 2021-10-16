"""
스타트와 링크
백준 14889번 문제 삼성 SW 역량 테스트 문제
"""
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
# 최소값 비교하기 위해 맨 처음에 엄청 큰 수를 줌
ans = 10000000
# 조합 만들기 위해서 멤버 넣어줌
mem = [i for i in range(n)]

for comb in list(combinations(mem, n//2)):
    # set을 통해 각각 start 조합 뽑아주고 나머지 조합들을 link로 보냄
    start = set(comb)
    link = set(mem) - start
    start = list(start)
    link = list(link)

    start_score = 0
    link_score = 0
    # 이미 팀의 조건을 각각 나누어 주었기 때문에 n//2를 통해서 팀원 명수만큼만 진행
    for i in range(1, n//2):
        for j in range(i):
            start_score += people[start[i]][start[j]] + people[start[j]][start[i]]
            link_score += people[link[i]][link[j]] + people[link[j]][link[i]]
            # print(score)
    ans = min(abs(start_score-link_score), ans)

print(ans)
