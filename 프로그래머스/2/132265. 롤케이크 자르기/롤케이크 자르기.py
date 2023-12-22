def solution(topping):
    from collections import Counter
    right = Counter(topping)
    answer = 0
    left = set()
    for t in topping :
        right[t] -= 1
        left.add(t)
        if right[t] == 0 :
            right.pop(t)
        if len(right) == len(left) :
            answer += 1
    return answer