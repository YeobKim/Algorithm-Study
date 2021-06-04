"""
숫자 카드 게임
N x M 형태로 카드가 놓여있는데 행마다 가장 작은 숫자를 열 마다 추출하여 그 중 큰 숫자를 뽑아낸다.
"""
n, m = map(int, input().split())
result = []

for i in range(n):
    data = list(map(int, input().split()))
    result.append(min(data)) # result라는 리스트에 min 값을 계속 저장하고

final = max(result) # for문이 끝나면 밖에서 가장 max 값을 뽑아냄

print(final)
