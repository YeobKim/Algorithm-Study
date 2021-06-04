people = list(map(int, input().split()))
limit = int(input())
people.sort()
boat = 0
cnt = 0
# print(len(people)-1)
for i in range(0, len(people) - 1, 2):
    if people[i] + people[i + 1] <= limit:
        boat += 1
        cnt += 2
    elif people[i] + people[i + 1] >= limit:
        boat += 2
        cnt += 2

    if cnt == len(people) - 1:
        boat += 1
print(boat)
