"""
만들 수 없는 금액
"""

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1 # 우선 타겟을 1로 초기값으로 정해서
for x in coins:
    if target < x: # x가 target보다 작으면 for문을 종료하고
        break
    else: # target과 같게 되면 x를 누적하면서 값을 
        target += x

print(target)
