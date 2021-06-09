"""
나무 자르기
나무를 자르는 길이를 정했을 때 잘라진 나무의 길이 합 만큼 가져가는 형식
나무의 수 : N, 집에 가져가는 나무의 길이 : M
떡볶이 & 랜선 문제와 유사 이분 탐색으로 풀 수 있다.
"""
n, m = map(int,input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    num = 0
    for data in trees:
        if data >= mid:
            num += data - mid
    if num >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
