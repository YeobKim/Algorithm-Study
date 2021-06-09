"""
숫자 카드 2
"""

n = int(input())
data = list(map(int, input().split()))

m = int(input())
data_m = list(map(int, input().split()))

result = []

for j in data_m:
    cnt = 0
    for i in data:
        if j == i:
            print(j, i)
            cnt += 1
        else:
            pass
    result.append(cnt)

print(result)
