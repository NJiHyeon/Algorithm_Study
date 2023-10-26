def solution(keymap, targets):
    result = []
    for target in targets :
        r = 0
        l = []
        for alpha in target :
            a = []
            for k in keymap :
                if alpha in k :
                    a.append(k.index(alpha)+1)
            if len(a) == 0 :
                l.append(0)
            else :
                l.append(min(a))
        if 0 in l :
            result.append(0)
        else :
            result.append(sum(l))
            

       
    real = []
    for r in result :
        if r==0 :
            real.append(-1)
        else :
            real.append(r)
    return real