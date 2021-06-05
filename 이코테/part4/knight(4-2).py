"""
왕실의 나이트
8x8 체스판과 같은 좌표 평면
나이트는 L자로만 이동할 수 있음. 정원 밖으로 나갈 수 없음.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
두 가지 경우로 움직일 수 있음.
행은 알파벳으로 a~h, 열은 숫자로 1~8까지 있음
a1을 입력하면 움직일 수 있는 경우의 수 2가지 출력
"""
input_data = input()

# 알파벳의 경우를 받아서 숫자로 변환
if input_data[0] == 'a':
    row = 1
elif input_data[0] == 'b':
    row = 2
elif input_data[0] == 'c':
    row = 3
elif input_data[0] == 'd':
    row = 4
elif input_data[0] == 'e':
    row = 5
elif input_data[0] == 'f':
    row = 6
elif input_data[0] == 'g':
    row = 7
else:
    row = 8

col = int(input_data[1])

result = 0
# 모든 방향에 대해서 설정하고
direc = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

# 이 부분에서 하나씩 탐색하면서 진행
for route in direc:
    drow = row + route[0]
    dcol = col + route[1]
    # 범위를 벗어나는 부분은 continue 통해 코드 진행 x
    if drow < 1 or dcol < 1 or drow > 7 or dcol > 7:
        continue
    # 코드가 넘어왔을 때만 result값 올려줌
    result += 1

print(result)
