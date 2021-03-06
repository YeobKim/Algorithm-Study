"""
프로그래머스 단속카메라 문제

[[-20,-15], [-14,-5], [-18,-13], [-5,-3]] 이와 같이 입력이 주어졌을 때,
내림차순으로 정렬을 하면 [[-5, -3], [-14, -5], [-18, -13], [-20, 15]] 이와 같이 만들어짐.
이 때 가장 처음의 [0]에 있는 값인 -5를 현재 위치라고 생각하고 다음의 [1]과 계속 비교
ex) -5에서 쭉 가다가 [-14,-5]에서는 -5에 걸려서 그냥 지나갈 수 있지만 [-18,-13]은 못 지나감.
    그렇게 되면 못 지나가는 쪽의 가장 먼 쪽에 카메라를 설치해줌.(다음의 효율성을 위해!)
"""

def solution(routes):
    answer = 1
    routes.sort(reverse=True)
    now = routes[0][0]
    
    for data in routes[1:]:
        if data[1] >= now:
            continue
        else:
            now = data[0]
            # print(now)
            answer += 1
            
    return answer
