def solution(n, k):
    import math
    '''
    from itertools import permutations
    jul = []
    j = 0
    for i in permutations([i for i in range(1, n+1)], n):
        j += 1
        if j == k :
            return i
    '''
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
    