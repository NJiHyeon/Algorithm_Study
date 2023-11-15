def solution(clothes):
    from itertools import combinations
    import math
    import collections
    cl=[]
    for c in clothes :
        cl.append(c[1])
    
    c_n = list(collections.Counter(cl).values())
    
    answer = 1
    for n in c_n :
        answer *= (n+1)

    return answer-1