"""
음료수 얼려 먹기
이코테 p.149
"""
n, m = map(int, input().split())
ice = []

for i in range(n):
    ice.append(list(map(int, input().split())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if ice[x][y] == 0:
        ice[x][y] = 1
        # 상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

"""
DFS 문제 음료수 얼려먹기
"""
n, m = map(int, input().split())

ice = []
for _ in range(n):
    ice.append(list(map(int, input())))

def dfs(x, y):
    if x >= n or x <= -1 or y >= m or y <= -1:
        return False
    if ice[x][y] == 0:
        # 해당 노드 방문 처리
        ice[x][y] == 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
