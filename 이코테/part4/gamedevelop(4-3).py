"""
게임 개발
NxM 크기의 직사각형에서 육지와 바다가 있다. 캐릭터는 동서남북 쪽을 바라본다.
(A, B) A->북쪽으로부터 떨어진 칸의 개수, B -> 서쪽으로부터 떨어진 칸의 개수

1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽방향으로 회전&왼쪽으로 한칸 전진
왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만하고 1단계로
3. 네 방향 모두 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유짛란 채로 한 칸 뒤로 가고 1단계로 돌아간다.
이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없으면 움직임 멈춤

"""
n, m = map(int, input().split())
x, y, direc = map(int, input().split())
arr = []

d = [[0] * m for _ in range(n)]
# 현재 위치에 대해 방문 처리
d[x][y] = 1

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# direc이 0:북, 1:동, 2:남, 3:서
def turn_left():
    global direc
    direc -= 1 # direc이 1일 때 동쪽인데 왼쪽으로 돌면 북쪽이 되기 때문에 direc에 -1을 해줌
    if direc == -1:
        direc = 3 # 북쪽일 때 왼쪽으로 돌면 서쪽이기 때문에 3으로 값을 바꿔줌

cnt = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direc]
    ny = y + dy[direc]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direc]
        ny = y - dy[direc]
        # 뒤로 갈 수 있다면 이동하기
        if arr[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(cnt)
