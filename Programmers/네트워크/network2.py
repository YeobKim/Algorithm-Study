"""
네트워크 문제 두 번째 풀이
덩어리를 구하는 문제인 <음료수 얼려먹기> 문제를 활용
그래프를 그려보니 덩어리 개수만큼 네트워크가 이루어지는 것을 발견
"""

n = int(input())
computers = []
for _ in range(n):
    computers.append(list(map(int, input())))

def dfs(x,y):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if computers[x][y] == 1:
        computers[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(len(computers)):
        if computers[i][j] == True:
            dfs(i, j)
            result += 1

print(result)
