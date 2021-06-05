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
elif input_data[0] == 'b':
    row = 6
else:
    row = 7

col = int(input_data[1])

result = 0
direc = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

for route in direc:
    drow = row + route[0]
    dcol = col + route[1]

    if drow < 1 or dcol < 1 or drow > 7 or dcol > 7:
        continue
    result += 1

print(result)
