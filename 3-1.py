# # 거스름돈 문제
# money = int(input())
# cnt = 0
# coins = [500, 100, 50, 10]
#
# for coin in coins:
#     cnt += money // coin # 몫을 구할 때 // 두번 써야한다.
#     money %= coin # 나머지를 반환하면서 500일 때 260 되고 100일 때 60되고 이런 식으로 진행
# print(cnt)

# # 1이 될 때까지
# n, k = map(int, input().split())
# print(n, k)
# cnt = 0
#
# while True :
#     if n % k == 0 :
#         n = n // k
#         cnt += 1
#         if n < k :
#             break
#     else:
#         n -= 1
#         cnt += 1
# print(cnt)

# 곱하기 혹은 더하기, 문자열을 받아 곱하기나 더하기를 하여 가장 큰 숫자를 반환
# 입력 받은 문자열 int로 변환해주는 것 주의하고 one을 결과 값으로 사용하는 것 생각하자!
data = input()
one = int(data[0])

for i in range(1, len(data)) :
    num = int(data[i])
    if num <= 1 or one <= 1:
        one += num
    else:
        one *= num
print(one)