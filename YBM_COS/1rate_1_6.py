"""
체스에서 나이트(knight)는 아래 그림과 같이 동그라미로 표시된 8개의 방향중 한 곳으로 한 번에 이동이 가능합니다.
단, 나이트는 체스판 밖으로는 이동할 수 없습니다.
체스판의 각 칸의 위치는 다음과 같이 표기합니다.

예를 들어, A번줄과 1번줄이 겹치는 부분은 'A1'이라고 합니다.
나이트의 위치 pos가 매개변수로 주어질 때, 나이트를 한 번 움직여서 이동할 수 있는 칸은 몇개인지 return 하도록 solution 함수를 완성해주세요.

---
매개변수 설명
나이트의 위치 pos가 solution 함수의 매개변수로 주어집니다.
- pos는 A부터 H까지의 대문자 알파벳 하나와 1 이상 8이하의 정수 하나로 이루어진 두 글자 문자열입니다.
- 잘못된 위치가 주어지는 경우는 없습니다.

---
return 값 설명
나이트를 한 번 움직여서 이동할 수 있는 칸의 개수를 return 해주세요.


"""

#You may use import as below.
#import math

def solution(pos):
    # Write code here.
    answer = 0
    # 각각의 방향을 정의
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    # 알파벳을 숫자로 바꿔주기 위해 index 값을 이용하는 배열 구성
    trans_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    
    # 숫자가 위에서부터 내려오기 때문에 기존에 우리가 알고 있는 배열로 맵핑해주기 위한 코드
    pos_y = 8 - int(pos[1])
    # 알파벳을 찾으면 pos_x에 숫자를 반환하며 반복문을 종료하여 더 이상 수행하지 않도록 함
    for i in range(len(trans_alpha)):
        if trans_alpha[i] == pos[0]:
            pos_x = i
            break
    
    # 정의한 방향 8개를 모두 돌면서
    for direc in range(8):
        x = pos_x + dx[direc]
        y = pos_y + dy[direc]
        # 범위를 벗어나면 count를 하지 않고
        if x < 0 or y < 0 or x >= 8 or y >= 8:
            continue
        # 범위 내에 있는 것만 count를 함    
        else:
            answer += 1

    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
