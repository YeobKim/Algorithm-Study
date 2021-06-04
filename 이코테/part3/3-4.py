"""
1이 될 때 까지
어떤 숫자 N이 주어졌을 때
1. N에서 1을 뺀다
2. N에서 K로 나눈다
두 조건으로 1이 될 때까지 수행한다. 2번 연산은 N이 K로 나누어 떨어질 때만 가능
"""
n, k = map(int, input().split())

result = 0

while True:
    if n == 1:
        break
    if n % k == 0:
        n = n/k
        result += 1
    else:
        n -= 1
        result += 1

print(result)
