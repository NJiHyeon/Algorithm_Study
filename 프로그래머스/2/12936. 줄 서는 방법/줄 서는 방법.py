def solution(n, k):
    import math
    origin = [i for i in range(1, n+1)]
    answer =[]
    d = n-1 # 4
    while True :
        a = k // (math.factorial(d)) # 3
        b = k % (math.factorial(d))  #18
        if b != 0:
            s = origin[a]
            answer.append(s)
            origin.remove(s)
            d -= 1
            k = b
        else:
            s = origin[a-1]
            answer.append(s)
            origin.remove(s)
            break
    answer += origin[::-1]
    return answer


# 시간초과
    from itertools import permutations
    jul = []
    j = 0
    for i in permutations([i for i in range(1, n+1)], n):
        j += 1
        if j == k :
            return i

# 다른 풀이
from math import factorial
    answer = []
    order = list(range(1,n+1))
    m = []
    while n!=0 :
        fact = factorial(n-1)
        #answer.append(order.pop(k//fact-1 if k%fact ==0 else k//fact))
        m.append([k-1, fact, (k-1)//fact])
        answer.append(order.pop((k-1)//fact))
        n,k = n-1, k%fact
    return m
    return answer
