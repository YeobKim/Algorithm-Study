"""
상어 초등학교
백준 21608번 문제 삼성 SW 역량테스트
"""
n = int(input())
data = [list(map(int, input().split())) for _ in range(n**2)]
classroom = [[0]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for stud in data:
    stud_num, favor_num = stud[0], stud[1:] # [0]에는 현재 학생의 번호, [1:]에는 [0]의 학생이 좋아하는 학생들의 번호가 쓰여있음.
    max_x = 0
    max_y = 0
    max_favor = -1
    max_empty = -1
    for i in range(n):
        for j in range(n):
            if classroom[i][j] == 0:
                favor_cnt = 0
                empty_cnt = 0
                for k in range(4): # 동서남북을 돌면서
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<n: # 범위 안에 있을 때 
                        if classroom[nx][ny] in favor_num: # 해당 번호가 favor_num 안에 있다면
                            favor_cnt += 1 # cnt의 개수를 올려줌
                        if classroom[nx][ny] == 0:
                            empty_cnt += 1
                if max_favor < favor_cnt or (max_favor == favor_cnt and max_empty < empty_cnt):
                    max_x = i
                    max_y = j
                    max_favor = favor_cnt
                    max_empty = empty_cnt

    classroom[max_x][max_y] = stud_num

result = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        for data_num in data:
            if data_num[0] == classroom[i][j]: # 학생의 정보가 일치할 때
                favor_num = data_num[1:] # favor_num을 반환할 수 있도록
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if classroom[nx][ny] in favor_num:
                    cnt += 1
        if cnt != 0:
            result += 10**(cnt-1)

print(result)"""
상어 초등학교
백준 21608번 문제 삼성 SW 역량테스트
"""
n = int(input())
data = [list(map(int, input().split())) for _ in range(n**2)]
classroom = [[0]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for stud in data:
    stud_num, favor_num = stud[0], stud[1:] # [0]에는 현재 학생의 번호, [1:]에는 [0]의 학생이 좋아하는 학생들의 번호가 쓰여있음.
    max_x = 0
    max_y = 0
    max_favor = -1
    max_empty = -1
    for i in range(n):
        for j in range(n):
            if classroom[i][j] == 0:
                favor_cnt = 0
                empty_cnt = 0
                for k in range(4): # 동서남북을 돌면서
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<n: # 범위 안에 있을 때 
                        if classroom[nx][ny] in favor_num: # 해당 번호가 favor_num 안에 있다면
                            favor_cnt += 1 # cnt의 개수를 올려줌
                        if classroom[nx][ny] == 0:
                            empty_cnt += 1
                if max_favor < favor_cnt or (max_favor == favor_cnt and max_empty < empty_cnt):
                    max_x = i
                    max_y = j
                    max_favor = favor_cnt
                    max_empty = empty_cnt

    classroom[max_x][max_y] = stud_num

result = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        for data_num in data:
            if data_num[0] == classroom[i][j]: # 학생의 정보가 일치할 때
                favor_num = data_num[1:] # favor_num을 반환할 수 있도록
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if classroom[nx][ny] in favor_num:
                    cnt += 1
        if cnt != 0:
            result += 10**(cnt-1)

print(result)
