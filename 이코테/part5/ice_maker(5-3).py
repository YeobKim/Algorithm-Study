"""
음료수 얼려먹기
NxM의 얼음 틀이 있는데 구멍이 나있는 부분은 -> 0, 칸막이는 -> 1로 표현
0이 뭉쳐 있는 부분이 얼어서 음료수를 얼릴 수 있는 부분, 얼음 덩어리의 개수를 세야함.

이러한 문제는 DFS로 풀 수 있음.
"""
n, m = map(int, input().split())

ice_box = []
for _ in range(n):
    ice_box.append(list(map(int, input())))

def dfs(x, y):
    # 주어진 범위를 벗어나면 종료할 수 있도록 선언
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면
    if ice_box[x][y] == 0:
        # 해당 노드에 대해 방문 처리
        ice_box[x][y] = 1
        # 상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)
