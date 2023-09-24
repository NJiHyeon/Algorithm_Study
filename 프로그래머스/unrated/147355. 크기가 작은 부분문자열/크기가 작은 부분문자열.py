def solution(t, p):
    l = len(p)
    m = []
    for i in range(0, len(t)-len(p)+1) :
        m.append(t[i:i+l])
    answer = 0
    for j in m :
        if j <= p :
            answer += 1
    return answer