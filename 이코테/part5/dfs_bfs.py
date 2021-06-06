"""
DFS
방문하는 노드에 방문 처리를 해주면서 진행
결을 잡으면 깊이 들어갔다가 모두 확인하고 나옴
"""
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표ㅕ현
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

"""
BFS
가장 가까운 것들부터 확인하고 나옴
큐를 이용해서 풀이 가능, 최단 경로 같은 문제 해결
"""
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표ㅕ현
visited = [False] * 9

bfs(graph, 1, visited)
