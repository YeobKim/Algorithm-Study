"""
럭키 스트레이트
게임에서 점수의 절반을 기준으로 나눴을 때 그 나눈 기준으로 왼쪽과 오른쪽의 합이 같으면 기술을 쓸 수 있음.
예를 들어 현재 점수가 123,402라면 절반을 기준으로 각 합이 6이기 때문에 Lucky를 반환
"""
n = input()

data = list(n)

data1 = data[0:len(data)//2]
data2 = data[len(data)//2:]

result1 = 0
result2 = 0

for i in range(len(data)//2):
    result1 += int(data1[i])
    result2 += int(data2[i])

if result1 == result2:
    print('Lucky')
else:
    print('Ready')
