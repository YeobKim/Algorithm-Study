"""
큰 수의 법칙
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단 배열의 특정 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다
예를 들어 순서대로 2,4,5,4,6으로 이루어진 배열이 있을 때 M이 8이고 K가 3이면
6+6+6+5+6+6+6+5인 46이 된다.
배열의 크기 n, 숫자가 더해지는 횟수 m, 연속해서 더해지는 최대 회수 k
"""
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
val1 = data[n-1]
val2 = data[n-2]
result = 0

while m != 0:
    for i in range(k):
        if m == 0:
            break
        result += val1
    result += val2
    m -= (k + 1)

print(result)