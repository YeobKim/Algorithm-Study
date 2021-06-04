"""
랜선 자르기
K개의 랜선을 가지고 있는 각각 길이가 제 각각
N개의 같은 길이의 랜선을 만들고 싶어서 K개의 랜선을 잘라서 만들어야함
예를 들어, 300cm 짜리 랜선에서 140cm 짜리 랜선을 두개 잘라내면 20cm 버려야함
이때 최대 랜선의 길이를 구하는 프로그램을 작성
"""
# 이진 탐색을 통해 풀이하는 것 기억

k, n = map(int, input().split())

data = []
for _ in range(k):
    lanlist = int(input())
    data.append(lanlist)

start, end = 1, max(data)

while start <= end:
    mid = (start + end) // 2
    line_sum = 0
    for i in data:
        line_sum += i // mid

    if line_sum >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
