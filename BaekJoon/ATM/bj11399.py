"""
ATM
N명의 사람들이 줄을 서있고 1~N까지 번호가 매겨져 있음
i번 사람이 돈을 인출하는데 걸리는 시간은 P_i 분이다.
N명의 사람에게 각각 P_i 시간이 주어졌을 대 각 사람이 돈을 인출하는데 필요한 시간의 최솟값
"""
n = map(int, input().split())
n_min = list(map(int, input().split()))
n_min.sort()

min_sum = 0
result = 0

for i in n_min:
    min_sum += i
    result += min_sum

print(result)
