"""
단지 번호 붙이기
백준 2667번 문제
"""

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

# print(arr)

def dfs(x, y):
    if x < 0 or x >= n or y >= n or y < 0:
        return False

    if arr[x][y] == 1:
        # 전역 변수 설정해서 함수 밖에서도 사용할 수 있도록 함
        global temp_res
        temp_res += 1
        arr[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


result = 0
num_info = []

for i in range(n):
    for j in range(n):
        # for문이 돌 때 마다 초기화 시켜서 누적되는 것을 방지
        temp_res = 0
        if dfs(i, j) == True:
            result += 1
            # 리스트에 세대 수를 저장해서 마지막에 결과 때 빼서 쓸 수 있도록 함.
            num_info.append(temp_res)

# 오름차순 정렬
num_info.sort()

print(result)
for data in num_info:
    print(data)
