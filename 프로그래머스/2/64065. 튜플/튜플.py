def solution(s):
    import collections
    answer = []
    s = s[1:-1]
    i = 0
    dig = ''
    while True :
        if i == len(s) :
            break

        if s[i].isdigit() :
            dig += s[i]
        else :
            if dig.isdigit() :
                answer.append(int(dig))
            dig = ''
        i += 1

    d = collections.Counter(answer)
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    
    final = []
    for dd in d :
        final.append(dd[0])
    
    return final