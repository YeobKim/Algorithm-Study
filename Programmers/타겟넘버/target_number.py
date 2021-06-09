"""
1이 더해지고 빼지고 이렇게 되는 과정을 그래프로 그릴 수 있고,
dfs를 통해 푸는 방법을 선택
"""
answer = 0
def solution(numbers, target):   
    n = len(numbers)
    def dfs(idx, result):
        if idx == n: # idx가 numbers의 길이와 같을 때는 탐색이 끝이 난 경우이기 때문에 다음과 같이 선언
            if result == target:
                global answer # global로 선언 해서 전역변수로 사용 가능하도록 선언
                answer += 1
        else:
            # 1에서 2혹은 0으로 갈 수 있기 때문에 result+numbers[idx]와 result-numbers[idx] 두 가지에 대해 탐색을 진행
            dfs(idx+1, result+numbers[idx]) 
            dfs(idx+1, result-numbers[idx])
    dfs(0,0) # numbers와 target이 0인 값일 때부터 
    return answer
