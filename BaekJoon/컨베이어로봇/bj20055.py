"""
컨베이어 벨트 위의 로봇 문제
백준 20055번
"""
from collections import deque
import sys

n, k = map(int, input().split())
arr = deque(map(int, input().split()))
robot = deque([0]*n)
ans = 1

while True:
    # .rotate() 함수를 사용하면 deque에서 컨베이어벨트 처럼 돌아간다. 리스트에서는 사용 불가!
    # 1단계
    arr.rotate(1)
    robot.rotate(1)
    # print(robot)
    robot[-1] = 0
    # 2단계
    for i in range(n-2, -1, -1):
        if robot[i] != 0 and robot[i + 1] == 0 and arr[i + 1] >= 1:
            arr[i+1] -= 1
            robot[i+1] = robot[i]
            robot[i] = 0
    robot[-1] = 0
    # 3단계
    if robot[0] == 0 and arr[0] > 0:
        robot[0] = 1
        arr[0] -= 1

    # 4단계
    cnt = 0
    # .count(n) n의 갯수를 세는 함수 이용해서 0의 갯수가 k개 일때 멈출 수 있도록 동작
    if arr.count(0) == k:
        break
    ans += 1

print(ans)
