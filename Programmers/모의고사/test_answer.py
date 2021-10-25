def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    answer = []
    answer_cnt = []
    
    for i in range(len(answers)):
        # i%len(p1)처럼 해서 정의한 p1의 길이보다 벗어난 answers가 들어오더라도 다시 시작하면서 반복할 수 있도록 구성
        if answers[i] == p1[i%len(p1)]:
            cnt1 += 1
        if answers[i] == p2[i%len(p2)]:
            cnt2 += 1
        if answers[i] == p3[i%len(p3)]:
            cnt3 += 1
    answer_cnt = [cnt1, cnt2, cnt3]
    
    max_score = max(answer_cnt)

    for person, score in enumerate(answer_cnt):
        if score == max(answer_cnt):
            answer.append(person+1)
        
    return answer
