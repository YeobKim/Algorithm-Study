"""
문자열 재정렬
문자와 숫자가 들어왔을 떄 문자는 정렬을 하고 숫자는 모두 더해서 뒤에 붙여준다.
"""
n = input()
alpha = []
num = 0

for i in n:
    if i.isalpha():
        alpha.append(i)
    else:
        num += int(i)

alpha.sort()
alpha.append(str(num))

print(''.join(alpha))
