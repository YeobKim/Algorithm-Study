"""
모험가 길드
"""
n = int(input())
data = list(map(int, input().split()))
data.sort()

cnt = 0
result = 0

for sp in data:
    cnt += 1
    print(cnt)
    if cnt >= sp:
        result += 1
        cnt = 0

print(result)
