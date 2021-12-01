"""
최소 공배수 구하는 문제
그냥 필요할 것 같아서 문제는 없지만 코드 구현

입력 => [4,8,20,25]
출력 => 200
"""

input_list = [4, 8, 20, 25]
multiple_num = 1

for num in input_list:
    multiple_num *= num

# 가장 큰 값부터 모두 곱한 값 까지 for문을 돌림
for num in range(max(input_list), multiple_num+1):
    cnt = 0
    for list_num in input_list:
        # num이 돌면서 input_list를 보면서 나머지가 0이면 cnt값을 올려주고
        if num % list_num == 0:
            cnt += 1
    # list를 다 돌았을 때 list의 길이와 같다면 즉, 모두 나누어 떨어진다면 for문 탈출 
    if cnt == len(input_list):
        answer = num
        break

print(answer)
