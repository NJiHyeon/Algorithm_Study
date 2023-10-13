def solution(k, m, score):
    score.sort(reverse=True)
    box = []
    l = len(score)
    for i in range(0, l+1, m) :
        box.append(score[i:i+m])
    
    total = 0
    for b in box :
        if len(b) == m :
            total += m*min(b)
            
    return total