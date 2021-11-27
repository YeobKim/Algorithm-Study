"""
자연수가 중복 없이 들어있는 리스트가 있습니다. 이 리스트에서 합이 K의 배수가 되도록 서로 다른 숫자 세개를 고르는 방법은 몇 가지인지 세려고 합니다.
자연수가 들어있는 리스트 arr가 매개변수로 주어질 때, 이 리스트에서 합이 K의 배수가 되도록 서로 다른 숫자 세개를 고르는 방법의 가짓수를 return 하도록 solution 함수를 완성해주세요.

---
매개변수 설명
자연수가 들어있는 리스트 arr가 solution 함수의 매개변수로 주어집니다.
- arr의 길이는 3 이상 100 이하입니다.
- arr에는 1 이상 1,000 이하의 자연수가 중복 없이 들어있습니다.
- K는 1 이상 10 이하의 자연수입니다.

---
return 값 설명
리스트에서 합이 K의 배수가 되도록 서로 다른 숫자 세개를 고르는 방법의 가짓수를 return 해주세요.
- 그러한 방법이 없다면 0을 return 하면 됩니다.

---
예시
  arr            	K   	return
  [1, 2, 3, 4, 5]	3   	4     
"""

#다음과 같이 import를 사용할 수 있습니다.
#import math
from itertools import combinations

def solution(arr, K):
    #여기에 코드를 작성해주세요.
    answer = 0
    # 조합을 통해서 3개를 뽑을 수 있는 경우의 수를 뽑아냄
    com_list = list(combinations(arr, 3))
    # 조합이 있는 리스트를 보면서
    for num_com in com_list:
        tmp = 0
        # tmp에 합을 저장
        for i in num_com:
            tmp += i
        # tmp가 만약 3으로 나누어 떨어진다면 갯수를 올려줌
        if tmp % 3 == 0:
            answer += 1

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
