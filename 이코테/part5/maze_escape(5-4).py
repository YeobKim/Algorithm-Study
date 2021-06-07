"""
미로 탈출
NxM 크기의 직사각형 형태의 미로가 있음
여러 마리의 괴물이 존재해 피해서 탈출해야 함.
현재 (1,1)에 있고 출구는 (N,M), 괴물이 있는 부분->0, 괴물이 없는 부분->1
결론 -> 1을 따라서 N,M까지 가야한다. 최단경로 문제 => BFS 사용해서 풀자!
"""
from collections import deque

n, m = map(int, input().split())

# 미로의 값들을 받아서 maze라는 리스트에 저장
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

# 이동할 네 방향에 대해 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌때까지 반복을 하는 것.
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 길이 아닌 경우
            if maze[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1]

print(bfs(0,0))
