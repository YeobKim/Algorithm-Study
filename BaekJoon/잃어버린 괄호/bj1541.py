"""
잃어버린 괄호
0~9, +, - 만으로 이루어진 식에서 괄호를 쳐서 가장 작은 수를 만드는 것
예를 들어 55-50+40의 식이 있다고 하면 55-(50+40)
"""
num = input().split('-')

result = 0

for i in num[0].split('+'):
    result += int(i)
for i in num[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
