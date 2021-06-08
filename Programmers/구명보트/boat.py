"""
구명보트 문제
limit이 100으로 설정되어 있어 최대한 많은 사람 수를 태워서 보트의 수를 최소화 하는 방법

큐를 이용해서 푸는데 우선 sort를 통해서 정렬을 시켜줌
1. 가장 무게가 많은 사람과 가장 무게가 적은 사람의 합이 limit 이하라면 보트 하나에 태우고 pop과 popleft
2. 가장 무게가 많은 사람과 가장 무게가 적은 사람의 합이 limit 초과라면 가장 무거운 사람만 태우고 pop
"""

from collections import deque

def solution(people, limit):
    people.sort()
    queue = deque(people)
    boat = 0
    
    while queue: # 큐에 요소가 있을 때만 동작
        if len(queue) >= 2: # 큐 안에 2명 이상이 들어있을 경우에만 동작
            if queue[0] + queue[-1] <= limit:
                queue.pop()
                queue.popleft()
                boat += 1
            elif queue[0] + queue[-1] > limit:
                queue.pop()
                boat += 1
        else: # 큐에 한명만 있으면 동작
            if queue[0] <= limit:
                queue.pop()
                boat += 1
        
    return boat
