def solution(sequence, k) :
    result = []
    r = 0
    l = 0
    s = 0
    while True :
        if s <= k :
            if r >= len(sequence) :
                break
            s += sequence[r]
            r += 1
        else :
            if l >= len(sequence) :
                break
            s -= sequence[l]
            l += 1
        if s==k :
            result.append([l, r-1])
    result.sort(key = lambda x : (x[1]-x[0], x[0]))
    return result[0]