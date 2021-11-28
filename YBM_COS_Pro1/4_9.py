"""
hour 시 minute 분에 아날로그 시계의 시침과 분침이 몇 도를 이루는지 계산하려 합니다. 예를 들어, 3시 00분에 시침과 분침은 90˚를 이룹니다.
어떤 시점의 시 hour, 분 minute이 매개변수로 주어질 때, hour 시 minute 분에 아날로그 시계의 시침과 분침이 이루는 각도를 소숫점 첫번째 자리까지 표현한 문자열을 return 하도록 solution 함수를 작성해주세요.

---
매개변수 설명
어떤 시점의 시 hour, 분 minute이 solution 함수의 매개변수로 주어집니다.
- hour는 1 이상 12 이하인 자연수입니다.
- minute은 0 이상 59 이하인 정수입니다.

---
return 값 설명
hour 시 minute 분에 아날로그 시계의 시침과 분침이 이루는 각도를 소숫점 첫번째 자리까지 표현한 문자열을 return 하세요.
- 단, 각도는 소수점 이하 첫째 자리까지 표현하세요.

---
예시
  hour	minute	return
  3   	0     	"90.0"
"""

# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(hour, minute):
    # 시계의 특성을 이용해보면
    # 360/12 => 정각일 때 30도, 또 30/60 -> 1분 지날 때 마다 0.5도 씩
    # 360/60 => 분당 6도
    hour_angle = 30*float(hour) + 0.5*float(minute)
    min_angle = 6*float(minute)
    
    # hour보다 min이 큰 각도를 가지고 있을 수 있기 때문에 절대값을 취해줌
    answer = abs(hour_angle-min_angle)
    
    # 다음과 같이 포맷팅해주어서 소수 첫째자리까지 반환이 될수 있도록 함
    return '{:.1f}'.format(answer)

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
hour = 3
minute = 0
ret = solution(hour, minute)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
