def solution(topping):
    answer = 0
    from collections import Counter
    top_r = Counter(topping)
    top_l = dict()
    for t in topping :
        top_r[t] -= 1
        top_l[t] = 1
        if top_r[t] == 0 :
            top_r.pop(t)
        if len(top_r) == len(top_l) :
            answer += 1
    return answer