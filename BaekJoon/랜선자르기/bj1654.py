"""
큰 수의 법칙
N개의 숫자가 입력되었을 때 M번 더해서 가장 큰 수를 뽑아내는데 K번까지만 연속해서 더해질 수 있다.
예를 들어, N이 5이고 M이 8이고 K가 3일 때, 2 4 5 4 6 의 숫자가 입력되었다고 할 때
6+6+6+5+6+6+6+5 = 46과 같이 결과가 도출되어야 한다.
"""
# 이진 탐색을 이용해야 하는 것 기억하기

N, M, K = map(int, input().split())

inlist = list(map(int, input().split()))

inlist.sort() # 숫자의 크기별로 가져오기 위해 먼저 sorting 한다.

num1 = inlist[N-1] # sorting이 되었기 때문이 N-1이 가장 큰 숫자가 되고
num2 = inlist[N-2] # N-2가 두 번째로 큰 숫자가 된다.
result = 0

for i in range(M): # M번 더 하는데
    if M == 0:
        break # M이 0이 되면 바로 break가 될 수 있도록 for문 시작 부분에 다음과 같이 선언
    for j in range(K):
        result += num1
    M -= K # K번 만큼 더해졌기 때문에 K만큼 빼줌
    result += num2
    M -= 1 # num2는 한번만 더해지기 떄문에 -1을 해줌

print(result)
