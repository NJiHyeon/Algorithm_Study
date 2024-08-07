import math

def solution(number, limit, power):
    n_list = []
    for i in range(1, number+1) :
        n_list.append(yak(i))    
    answer = 0
    for l in n_list :
        if l <= limit :
            answer += l
        else :
            answer += power
    return answer


def yak(i) :
    n = 0
    for j in range(1, int(math.sqrt(i)) + 1) :
        if i%j == 0 :
            if j != i//j :
                n += 2
            else :
                n += 1
    return n