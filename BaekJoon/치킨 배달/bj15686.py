"""
치킨 배달
백준 15686번 문제 삼성 SW 역량 테스트
"""
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
comb_arr = []
result = 10000 # 최소값 비교하기 위해 임의로 큰 값을 줌

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            # 치킨 집의 좌표를 구하기 위해서 city 내의 2인 부분의 좌표를 모두 chicken 배열에 저장
            chicken.append((i, j))
            
# 조합대로 구해야하니까 조합의 경우의 수를 모두 뽑아냄
for com in combinations(chicken, m):
    comb_arr.append(com)

# city를 보면서 1일 때 조합에 있는 치킨집들과의 거리를 구함
# 최소값 계속 저장하면서 갱신하도록 구성
for data in comb_arr:
    distance = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                dis_res = 10000 # 최소값 비교하기 위해 임의로 큰 값을 줌
                for k in data: # k는 (1,2) 이런 식으로 조합의 따른 치킨집의 좌표 들어있음
                    x_dis = abs(i - k[0])
                    y_dis = abs(j - k[1])
                    dis_res = min(dis_res, x_dis+y_dis)
                distance += dis_res
    result = min(result, distance)

print(result)
