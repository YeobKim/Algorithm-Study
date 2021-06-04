# 모험가 길드
n = int(input())
scare = list(map(int, input().split()))
scare.sort()
cnt = 0
result = 0

for i in scare:
    cnt += 1
    # 공포도가 현재인원 이하일 때 그 인원 그룹에 포함시킨다.
    if cnt >= i:
        result += 1
        cnt = 0

print(result)

# 곱하기 혹은 더하기
number = str(input())
result = int(number[0])

for i in range(1, len(number)):
    num = int(number[i])
    if num <= 1 or result <= 1:
        result += int(number[i])
    else:
        result *= int(number[i])

print(result)

# 문자열 뒤집기
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] == data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

# 만들 수 없는 금액
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for data in coins:
    if target < data:
        break
    target += data

print(target)

# 볼링공 고르기
from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))
ballscombine = list(combinations(balls, 2))

result = len(ballscombine)
# print(result)

for data in ballscombine:
    if data[0] == data[1]:
        result -= 1

print(result)
