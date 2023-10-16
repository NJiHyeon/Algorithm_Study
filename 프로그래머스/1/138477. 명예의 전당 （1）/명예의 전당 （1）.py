def solution(k, score):
    top = []
    ann = []
    for i in range(len(score)) :
        if i < k :
            top.append(score[i])
            top.sort(reverse=True)
            ann.append(top[-1])
        else :
            if score[i] > top[-1] : 
                top.pop(-1)
                top.append(score[i])
                top.sort(reverse=True)
                ann.append(top[-1])
                
            else :
                ann.append(top[-1])
    

    '''
    for i in range(k) :
        top.append(score[i])
        top.sort(reverse=True)
        ann.append(top[-1])
    
    for i in range(k, len(score)) :
        if score[i] > top[-1] : 
            top.pop(-1)
            top.append(score[i])
            top.sort(reverse=True)
            ann.append(top[-1])
        else :
            ann.append(top[-1])
    '''
    return ann