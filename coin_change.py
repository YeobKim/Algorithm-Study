"""
# 거스름 돈 문제
500, 100, 50, 10원 짜리 동전이 있는데 거슬러줄 돈을 동전으로 거슬러 준다고 할 때
거슬러 줄 수 있는 동전의 최소 갯수 구하기
"""
money = int(input())
coins = [500, 100, 50, 10]
result = 0

for i in coins:
    result += money // i
    money %= i

print(result)