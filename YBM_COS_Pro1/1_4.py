"""
어느 누군가가 타임머신을 타고 과거로 가서 숫자 0이 없는 수 체계를 전파했습니다. 역사가 바뀌어 이제 사람들의 의식 속엔 0이란 숫자가 사라졌습니다. 
따라서, 현재의 수 체계는 1, 2, 3, ..., 8, 9, 11, 12, ...와 같이 0이 없게 바뀌었습니다.
0을 포함하지 않은 자연수 num이 매개변수로 주어질 때, 이 수에 1을 더한 수를 return 하도록 solution 함수를 완성해주세요.

---
매개변수 설명
자연수 num이 solution 함수의 매개변수로 주어집니다.
- num은 1 이상 999,999,999,999,999,999 이하의 0을 포함하지 않는 자연수입니다.

---
return 값 설명
자연수 num에 1을 더한 수를 return 해주세요.

---
예시
  num    	return 
  9949999	9951111

"""
#You may use import as below.
#import math

def solution(num):
    # Write code here.
    # 조건에서 주어진 대로 우선 1 더하기
    num += 1

    # num에 있는 0의 갯수를 세기 위해 count 내장함수를 이용하기 전 str로 변환
    tmp = str(num)
    # 0의 갯수를 세준 후
    zero_cnt = tmp.count('0')
    # 0의 갯수만큼 1을 생성
    plus_digit = '1'*zero_cnt
    # 생성된 plus_digit을 int로 변환
    plus = int(plus_digit)
    
    # 최종적으로 1111을 더해줌
    answer = num + plus

    return answer


#The following is code to output testcase.
num = 9949999;
ret = solution(num)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
