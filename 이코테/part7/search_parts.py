"""
부품 찾기
손님이 부품을 찾으면 가게에 있는 부품에서 번호를 찾아
있으면 yes, 없으면 no 출력하기
"""
n = int(input())
part_data = list(map(int, input().split()))

m = int(input())
guest_data = list(map(int, input().split()))

for i in guest_data:
    if i in part_data:
        print('yes', end=' ')
    else:
        print('no', end=' ')
