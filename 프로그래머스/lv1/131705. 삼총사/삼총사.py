from itertools import combinations
def solution(number):
    perm = list(combinations(number, 3))
    answer = 0
    for p in perm :
        if sum(p) == 0 :
            answer += 1
    return answer