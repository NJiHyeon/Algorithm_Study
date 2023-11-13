def solution(n):
    step = [0]*(n+1)
    step[0] = 1
    step[1] = 1
    if n>=2 :
        for i in range(2, n+1) :
            step[i] = step[i-1]+step[i-2]
        return step[-1]%1234567
    else :
        return step[-1]