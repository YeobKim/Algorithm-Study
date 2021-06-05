"""
상하좌우
L, R, U, D에 따라 움직이면서 진행하는데 
주어진 N이 전체 지도의 크기라고 할 때 벗어나면 안되는 코드를 작성
"""

n = int(input())
move_type = list(map(str, input().split()))

x, y = 1, 1
# L R U D 순으로 dx, dy 저장
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in move_type:
    if plan == 'L':
        nx = x + dx[0]
        ny = y + dy[0]
    elif plan == 'R':
        nx = x + dx[1]
        ny = y + dy[1]
    elif plan == 'U':
        nx = x + dx[2]
        ny = y + dy[2]
    else:
        nx = x + dx[3]
        ny = y + dy[3]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    x, y = nx, ny

print(x, y)
