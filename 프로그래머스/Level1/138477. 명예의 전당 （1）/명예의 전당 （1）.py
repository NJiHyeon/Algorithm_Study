def solution(k, score):
    top = []
    ann = []
    for i in range(len(score)) :
        # i가 k보다 작으면 top에서 제거없이 계속 추가
        if i < k :
            top.append(score[i])
            top.sort(reverse=True)
            ann.append(top[-1])
        # i가 k보다 크거나 같아지면 제일 점수가 작은 것 제거 후 추가해서 sort
        else :
            if score[i] > top[-1] : 
                top.pop(-1)
                top.append(score[i])
                top.sort(reverse=True)
                ann.append(top[-1])
                
            else :
                ann.append(top[-1])

    return ann