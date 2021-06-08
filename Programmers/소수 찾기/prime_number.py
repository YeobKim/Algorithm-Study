from itertools import permutations
import math

def check(n):
    k = math.sqrt(n)
    if n < 2: 
        return False
    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1,len(numbers)+1):
        num_per = list(map(''.join, permutations(numbers, i)))
        for x in set(num_per): # set을 사용해서 중복되는 숫자를 없애주는 역할
            if check(int(x)) == True:
                answer.append(int(x))
    answer = len(set(answer))
    
    return answer
