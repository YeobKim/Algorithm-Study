"""
마법사 상어와 비바라기
백준 21610번 문제 삼성 SW 역량테스트
"""

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
moves = []
for i in range(m):
    tmp = list(map(int, input().split()))
    moves.append([tmp[0] - 1, tmp[1]]) # dx, dy 정보에 맞춰주기 위해서 temp[0]-1을 해줌

# 초기에 주는 정보는 리스트나 밖에서 정의할 수 있는지 확인 해보기!
clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

# 모든 방향의 x,y 좌표 설정
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for i in range(m):
    # step 1
    move = moves[i]
    next_clouds = []
    # 구름의 크기가 정해진 것이 아니니까 range(정해진 숫자) 넣어서 풀지 않기! 구름의 정보가 두 번째에서 바뀔 수 있다.
    for cloud in clouds:
        x = cloud[0]
        y = cloud[1]
        d = move[0]
        s = move[1]
        nx = (n + x + dx[d] * s) % n # n의 나머지 값으로 해주면서 n이 넘었을 때 1부터 다시 시작하도록! 핵심코드
        ny = (n + y + dy[d] * s) % n
        next_clouds.append([nx, ny])

    # step 2.
    visited = [[False] * n for _ in range(n)] # 구름이 머물었는지 여부를 판단해주기 위해 선언
    for cloud in next_clouds:
        x = cloud[0]
        y = cloud[1]
        arr[x][y] += 1
        visited[x][y] = True # 해당 영역에 구름이 머물었다는 것을 저장

    # step 3
    clouds = [] # 구름을 비워주는 코드

    # step 4
    # 대각선 방향 설정
    x_cross = [-1, -1, 1, 1]
    y_cross = [-1, 1, -1, 1]
    for cloud in next_clouds:
        x = cloud[0]
        y = cloud[1]
        count = 0
        for i in range(4):
            nx = x + x_cross[i]
            ny = y + y_cross[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] >= 1:
                count += 1

        arr[x][y] += count

    # step 5
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and visited[i][j] == False:
                arr[i][j] -= 2
                clouds.append([i, j]) # 방문하지 않은 곳에 대해 좌표를 저장

ans = 0
for i in range(n):
    ans += sum(arr[i])

print(ans)
