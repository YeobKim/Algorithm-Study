"""
수 정렬하기(브론즈1)
N개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램 작성
수는 중복x
"""
n = int(input())

num = [int(input()) for _ in range(n)]

num.sort()
result = []

# 중복검사 하는 부분
for x in num:
    if x in result:
        pass
    else:
        result.append(x)
        print(x)
