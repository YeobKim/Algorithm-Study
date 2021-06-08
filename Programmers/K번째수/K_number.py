# def solution(array, commands):
#     buffer = []
#     answer = []
#     for val in commands:
#         for i in range(val[0] - 1, val[1]):
#             buffer.append(array[i])
#         buffer.sort()
#         answer.append(buffer[val[2] - 1])
#         buffer =[]
#     return answer
array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1,7,3]]

buffer = []
answer = []
for val in commands:
    # i = val[0] # 2
    # j = val[1] # 5
    # k = val[2] # 3
    for i in range(val[0] - 1, val[1]):
        buffer.append(array[i])
    buffer.sort()
    answer.append(buffer[val[2] - 1])
    buffer =[]

print(answer)
