"""
주유소
어떤 나라에 N개의 도시가 있다. 도시들은 일직선 도로 위에 있다.
처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름 넣고 출발
1km 마다 1리터의 기름을 사용, 각 도시에는 단 하나의 주유소가 있고 도시마다 주유소 리터당 가격은 다름.
입력으로 첫번째 줄은 도시의 개수, 두번째 줄은 두 도시를 연결하는 도로의 길이, 세번째 줄은 주유소의 리터당 가격
"""
n = int(input()) # 4
load_len = list(map(int, input().split())) # 2 3 1
oil_val = list(map(int, input().split())) # 5 2 4 1

result = 0
cost1 = oil_val[0]

for i in range(len(load_len)):
    if oil_val[i] <= cost1:
        cost1 = oil_val[i]
    result += cost1 * load_len[i]

print(result)
