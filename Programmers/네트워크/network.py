"""
네트워크 문제
컴퓨터가 서로 연결이 되어있으면 네트워크가 이루어졌다고 할 수 있는데 간접적으로 연결되어 있어도 하나의 네트워크로 봄
예를 들어, A-B가 연결되어 있고 B-C가 연결되어 있으면 A-B-C가 하나의 네트워크임
DFS를 이용해서 풀 수 있음
"""
def dfs(n, computers, com, visited):
    visited[com] = True # DFS에 들어왔기 때문에 현재 com에 대해 방문 처리
    for i in range(n): # 현재 컴퓨터 외의 다른 컴퓨터와의 연결을 보는 것
        if i != com and computers[com][i] == 1: # 검색하고 있는 것이 현재 컴퓨터가 아니고 현재 컴퓨터와 연결이 되어 있고
            if visited[i] == False: # 방문처리가 되어있지 않다면
                dfs(n, computers, i, visited) # DFS를 수행하면서 
                
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)] # 우선 방문을 판별하는 list를 만들고 초기값을 모두 False로 지정
    for com in range(n): # n개의 컴퓨터를 검색하는데
        if visited[com] == False: # 그 컴퓨터의 상태가 False라면
            dfs(n, computers, com, visited) # DFS를 수행한다
            answer += 1
    return answer
