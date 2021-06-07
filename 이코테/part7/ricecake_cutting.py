"""
떡볶이 떡 만들기
떡의 개수를 N, 요청한 떡의 길이 M 이 주어졌을 때
절단기의 높이를 최대로 설정하는 것이 출력값으로..
"""
n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))
rice_cake.sort()

start = 0
end = max(rice_cake)

result = 0
while start <= end:
    len_sum = 0
    mid = (start + end) // 2
    for x in rice_cake:
        if x > mid: # 떡의 길이가 자르는 만큼보다 클 때만 동작할 수 있도록
            len_sum += x - mid
    if len_sum >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
