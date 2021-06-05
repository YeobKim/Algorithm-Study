"""
동전 0
동전의 종류는 총 N종류, 각각의 동전을 매우 많이 가지고 있음.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 할 때 필요한 동전 개수 최솟값 구하기
동전의 종류 N과 가치의 합 K를 첫줄에 받고,
두 번째 줄부터 N개의 동전의 가치
"""
n, k = map(int, input().split())
coins = []
result = 0

for _ in range(n):
    data = int(input())
    coins.append(data)

coins.sort(reverse=True)

for i in coins:
    if k // i >= 1:
        result += k//i
        k %= i

print(result)
