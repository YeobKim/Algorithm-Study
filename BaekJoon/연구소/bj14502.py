"""
연구소 문제
삼성전자 SW 역량테스트 이코테 p.341
백준 14502번 문제
"""
n, m = map(int, input().split())

lab = []

for _ in range(n):
    lab.append(list(map(int, input().split())))

temp = [[0]*m for _ in range(n)]

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                cnt += 1
                dfs(cnt)
                lab[i][j] = 0
                cnt -= 1

dfs(0)
# print(temp)
print(result)
