"""
곱하기 혹은 더하기
숫자가 입력되는 것을 곱하거나 더해서 가장 큰 숫자를 만드는 것
0이 나올 때만 더해주면 되는 것이므로 0에 주의해서 작성
"""

data = input()
result = 0

for i in range(len(data)):
    if data[i] == '0' or data[i-1] == '0' or i == 0:
        result += int(data[i])
    else:
        result *= int(data[i])
        
print(result)
