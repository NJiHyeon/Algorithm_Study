def solution(d, budget):
    d.sort()
    answer = 0
    for dd in d :
        if budget >= dd :
            answer += 1
            budget -= dd
        else :
            break
    return answer
