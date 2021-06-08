def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    answer = []
    answer_cnt = []
    
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            cnt1 += 1
        if answers[i] == p2[i]:
            cnt2 += 1
        if answers[i] == p3[i]:
            cnt3 += 1
    answer_cnt = [cnt1, cnt2, cnt3]
    
    for person, score in enumerate(answer_cnt):
        if score == max(answer_cnt):
            answer.append(person+1)
        
    return answer
