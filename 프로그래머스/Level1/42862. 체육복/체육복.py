def solution(n, lost, reserve):
    reserve, lost = list(set(reserve)-set(lost)), list(set(lost)-set(reserve)) #key point!
    s = []
    for l in lost :
        s.append(l)
        for r in reserve :
            if abs(l-r)==1 :
                s.pop()
                del reserve[reserve.index(r)]
                break
    
    return n-len(s)



