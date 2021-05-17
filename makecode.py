# # 럭키 스트레이트
# # 입력 받은 숫자를 절반으로 나눠 각각 더한 값이 같으면 LUCKY, 다르면 READY
# data = input()
# half = len(data) // 2
# result1 = 0
# result2 = 0
#
# for i in range(len(data)):
#     if i < half:
#         result1 += int(data[i])
#     else:
#         result2 += int(data[i])
#
# if result1 == result2 :
#     print("LUCKY")
# else:
#     print("READY")

# 문자열 재정렬
data = input()
alphabet = []
number = 0

for i in data:
    if i.isalpha() == True:
        alphabet += i
    else:
        number += int(i)

alphabet.sort()

final = alphabet + list(str(number))
print(''.join(final))