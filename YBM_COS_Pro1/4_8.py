"""
1 이상 9 이하 숫자가 적힌 카드를 이어 붙여 숫자를 만들었습니다. 이때, 숫자 카드를 조합해 만든 수 중에서 n이 몇 번째로 작은 수인지 구하려 합니다.
예를 들어, 숫자 카드 1, 2, 1, 3로 만들 수 있는 수를 작은 순으로 나열하면 [1123, 1132, 1213, 1231, 1312, ... , 3121, 3211]입니다. 
n이 1312라면, 숫자 카드를 조합해 만든 수 중 n은 n은 5번째로 작은 수입니다.
숫자 카드를 담은 리스트 card, 수 n이 매개변수로 주어질 때 숫자 카드를 조합해 만든 수 중에서 n이 몇 번째로 작은 수인지 return 하도록 solution 함수를 완성해주세요.

---
매개변수 설명
카드에 적힌 숫자를 담은 리스트 card, 수 n이 solution 함수의 매개변수로 주어집니다.
- card는 길이가 9 이하인 리스트입니다.
- card의 원소는 1 이상 9 이하인 자연수입니다.
- n은 999,999,999 이하인 자연수입니다.
- n의 자릿수는 리스트 card의 길이와 같습니다.
- n의 각 자리의 숫자는 1 이상 9 이하입니다.

---
return 값 설명
숫자 카드를 조합해 만든 수 중에서 n이 몇 번째로 작은 수인지 return 해주세요.
- 만약, n을 만들 수 없다면 -1을 return 해주세요.

---
예시
  card        	n   	return
  [1, 2, 1, 3]	1312	5     
  [1, 1, 1, 2]	1122	-1    
"""

# 다음과 같이 import를 사용할 수 있습니다.
# import math
from itertools import permutations

def solution(card, n):
    # 여기에 코드를 작성해주세요.
    answer = 0
    result = []
    # 순열을 통해서 조합될 수 있는 수를 모두 뽑아줌
    comb_card = list(permutations(card, 4))

    for per in comb_card:
        # 가장 먼저 오는 수가 예제의 기준으로 1000의 자리이기 떄문에 k를 다음과 같이 설정
        k = len(card) - 1
        num = 0
        for i in per:
            # k를 줄여나가면서 더해주면 숫자로 만들 수 있음
            num += i*(10**k)
            k -= 1
        # num이 이미 result에 존재하는 값이라면 for문 처음으로 돌아가서 다시 수행
        if num in result:
            continue
        # num이 없을 때는 result에 넣어줌
        result.append(num)
    
    # result 정렬
    result.sort()
    
    # n이 result에 있다면 몇 번째로 작은 수인지 sort된 result에서 보고 i+1의 값을 answer에 저장
    if n in result:
        for i in range(len(result)):
            if result[i] == n:
                answer = i+1
    # n이 result에 없으면 -1을 반환할 수 있도록 
    else:
        answer = -1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
