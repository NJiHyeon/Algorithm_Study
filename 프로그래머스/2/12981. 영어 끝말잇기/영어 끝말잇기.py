def solution(n, words):
    answer = []
    p = 1
    r = 1
    for i in range(1, len(words)) :
        p += 1
        if words[i] in words[:i] or words[i-1][-1]!=words[i][0] :
            answer.append(p)
            answer.append(r)
            break
        if p==n :
            p=0
            r+=1
    
    if len(answer)!=0 :
        return answer
    else :
        return [0,0]