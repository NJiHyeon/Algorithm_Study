def solution(X, Y):
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
        if new[0][0] != '0' :
            for i in range(len(new)) :
                answer += new[i]
        else :
            answer = '0'
    else :
        answer = '-1'
    return answer