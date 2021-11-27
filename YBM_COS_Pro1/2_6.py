"""
로봇이 2차원 평면의 원점 (0, 0)에 서있습니다. 
이 로봇은 x축 방향, 혹은 y축 방향으로만 움직일 수 있으며, 알파벳으로 명령을 내릴 수 있습니다. 명령을 내릴 때 사용하는 알파벳은 'L', 'R', 'U', 'D'의 4가지이며, 'L'은 x축 방향으로 -1만큼, 'R'은 x축 방향으로 +1만큼, 'U'는 y축 방향으로 +1만큼, 'D'는 y축 방향으로 -1 만큼 이동하라는 의미입니다. 
로봇에게 내린 명령이 순서대로 들어있는 문자열 commands가 매개변수로 주어질 때, 주어진 명령을 모두 수행한 후의 로봇 위치를 return 하도록 solution 함수를 완성해주세요.

---
매개변수 설명
로봇에게 내린 명령이 순서대로 들어있는 문자열 commands가 solution 함수의 매개변수로 주어집니다.
- commands는 알파벳 대문자 'L', 'R', 'U', 'D'로만 이루어진 문자열이며, 길이는 1 이상 100 이하입니다.

---
return 값 설명
주어진 명령을 모두 수행한 후의 로봇 위치를 return 해주세요.
- [x축 좌표, y축 좌표] 형태로 로봇의 최종 위치를 리스트에 담아 return 해주세요.

---
예시
  commands	return 
  "URDDL" 	[0, -1]
"""

#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(commands):
    # 여기에 코드를 작성해주세요.
    answer = [0, 0]
    
    # commands에서 들어오는 방향과 방향에 대한 x,y의 벡터값을 정의
    direc_alpha = ['L', 'R', 'U', 'D']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # commands의 문자들을 하나씩 보면서
    for com in commands:
        for i in range(len(direc_alpha)):
            # 일치할 때의 direc_alpha의 index값을 사용할 수 있도록 함
            if com == direc_alpha[i]:
               # index값에 dx, dy를 맵핑해두었기 때문에 다음과 같이 기존에 있던 answer의 값에 더해서 계속 값이 누적될 수 있도록 함
               answer[0] += dx[i]
               answer[1] += dy[i]

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
