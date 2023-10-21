def solution(X, Y):
    #x = list(map(int, X.split('')))
    #y = list(map(int, Y.split('')))
    x = [X[i] for i in range(len(X))]
    y = [Y[i] for i in range(len(Y))]
    sx = list(set(x))
    sy = list(set(y))

    new = []
    answer = ''
    for i in sx :
        for j in sy :
            if i==j  :
                new.append(i*min(x.count(i), y.count(j)))
                
                
    if len(new) > 0 :
        new.sort(reverse=True)
        '''
        r = list(set(new))
        rr = [r[0][i] for i in range(len(r[0]))]
        if list(set(new)) == ['0'] :
            answer = '0'
        elif list(set(rr)) == ['0'] :
            answer = '0'
        else :
            for i in range(len(new)) :
                answer += new[i]
        '''       
        if new[0][0] != '0' :
            for i in range(len(new)) :
                answer += new[i]
        else :
            answer = '0'
    else :
        answer = '-1'
    return answer