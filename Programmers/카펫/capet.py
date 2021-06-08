import math

def solution(brown, yellow):
    answer = []
    k = math.sqrt(yellow)
    for k in range(1, int(k) + 1):
        if yellow % k == 0:
            yellow_num = yellow // k
            if 2*(k+yellow_num) + 4 == brown:
                answer = [int(yellow_num)+2, k+2]
    return answer
