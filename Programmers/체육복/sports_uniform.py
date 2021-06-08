def solution(n, lost, reserve):
    per_num = len(lost)
    for x in lost:
        if x in reserve:
            per_num -= 1
            reserve.remove(x)
        elif (x - 1 in reserve):
            per_num -= 1
            reserve.remove(x-1)
        elif (x + 1 in reserve):
            per_num -= 1
            reserve.remove(x+1)
                
    result = n - per_num
    return result
