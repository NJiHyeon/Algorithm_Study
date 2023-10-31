def solution(survey, choices):
    cho = []
    i = 0
    for s in survey :
        score = [[], [], [], [], [], [], []]
        score[0].append(s[0])
        score[0].append(3)
        score[1].append(s[0])
        score[1].append(2)
        score[2].append(s[0])
        score[2].append(1)
        score[3].append(0)
        score[4].append(s[1])
        score[4].append(1)
        score[5].append(s[1])
        score[5].append(2)
        score[6].append(s[1])
        score[6].append(3)
        
        # choice
        cho.append(score[choices[i]-1])
        i += 1
        
    # 
    r = t = c = f = j = m = a = n = 0
    for ch in cho :
        if ch[0] == 'R' :
            r += ch[1]
        if ch[0] == 'T' :
            t += ch[1]
        if ch[0] == 'C' :
            c += ch[1]
        if ch[0] == 'F' :
            f += ch[1]
        if ch[0] == 'J' :
            j += ch[1]
        if ch[0] == 'M' :
            m += ch[1]
        if ch[0] == 'A' :
            a += ch[1]
        if ch[0] == 'N' :
            n += ch[1]
    
    answer = ''
    if r > t or r==t :
        answer += 'R'
    else :
        answer += 'T'
    
    if c>f or c==f :
        answer += 'C'
    else :
        answer += 'F'
        
    if j>m or j==m :
        answer += 'J'
    else :
        answer += 'M'
        
    if a>n or a==n :
        answer += 'A'
    else :
        answer += 'N'
    return answer