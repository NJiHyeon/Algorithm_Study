def solution(n, m, section):
    paint = 1
    start = section[0]
    for i in range(len(section)) :
        if section[i] - start >= m :
            paint += 1
            start = section[i]
    return paint