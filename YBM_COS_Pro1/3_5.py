"""
핸드폰 화면에 문구를 출력해주는 전광판 어플이 있습니다. 문구는 "happy-birthday"로 설정하였습니다. 전광판 어플은 다음과 같은 규칙으로 화면에 문구를 출력해 줍니다.
- 어플은 화면에 14자 문구를 출력합니다.
- 문구는 1초에 왼쪽으로 한 칸씩 움직입니다.
- 문구 이외의 부분은 "_"로 표시됩니다.
- 어플은 설정한 문구를 화면에 반복해 출력합니다. 
- 어플은 문구가 다 지나가면 설정한 문구를 반복해 보여줍니다.
    예를 들어, 처음에는 화면에 "______________"가 보입니다.
    3초 뒤에는 화면에 "___________hap"가 보입니다.
    14초 뒤에는 화면에 "happy-birthday"가 보입니다.
    20초 뒤에는 화면에 "birthday_____"가 보입니다.
    28초 뒤에는 모든 문자열이 지나간 후 "______________"가 보입니다.
    29초 뒤에는 다시 첫 번째 문자부터 나타나며, "_____________h"가 보입니다.
문구를 담은 문자열 phrases와 초를 담은 second가 매개변수로 주어질 때, 화면에 보이는 문자열을 출력하도록 solution 함수를 작성해 주세요.
단, '_'는 공백을 나타냅니다.

---
매개변수 설명
문구를 담은 문자열 phrases와 초를 담은 second가 solution 함수의 매개변수로 주어집니다.
- phrases는 "happy-birthday"입니다.
- second는 1 이상 10,000 이하인 자연수입니다.

---
return값 설명
solution 함수는 화면에 보이는 문자열을 return 합니다.

---
예시
  phrases         	second	return  
  "happy-birthday"	3     	"___hap"
"""
# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(phrases, second):
    # 여기에 코드를 작성해주세요.
    # 14개 까지만 써진다고 했으니까 14-second으로 _의 갯수를 정의
    answer = '_' * (14-second)
    # 나머지 글자들을 second만큼 phrases의 글자를 가져옴
    for i in range(second):
        answer += phrases[i]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
