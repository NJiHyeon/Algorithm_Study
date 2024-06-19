def solution(n):
    answer = [0, 1]
    for i in range(n-1) :
        nn = answer[-1]+answer[-2]
        answer.append(nn)
    return answer[-1]%1234567