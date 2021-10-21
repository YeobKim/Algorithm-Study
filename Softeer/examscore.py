"""
Softeer 성적 평균 문제
N명의 학생들의 성적이 학번순서대로 주어졌다. 학번 구간 [A, B]가 주어졌을 때 이 학생들 성적의 평균을 구하는 프로그램을 작성하라.

첫 번째 줄에 학생 수 N과 구간 수 K가 주어진다. 두 번째 줄에는 학생의 성적 Si (1 ≤ i ≤ N)가 주어진다. i + 2 (1 ≤ i ≤ K)번째 줄에는 i번째 구간 Ai, Bi가 주어진다.

입력은 다음 조건을 만족한다.
    1 ≤ N ≤ 106 인 정수
    1 ≤ K ≤ 104 인 정수
    1 ≤ Si ≤ 100 인 정수
    1 ≤ Ai ≤ Bi ≤ N

i번째 줄에 i번째 구간의 성적평균(소수셋째자리에서 반올림)을 출력한다. (차이가 0.01이하이면 정답으로 채점됨)
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
score = list(map(int, input().split()))

stud_num = [list(map(int, input().split())) for _ in range(m)]

for num in stud_num:
    score_avg = 0
    num_sum = 0
    for i in range(num[0]-1, num[1]):
        score_avg += score[i]
        num_sum += 1
    print('%.2f' % (score_avg/num_sum))
