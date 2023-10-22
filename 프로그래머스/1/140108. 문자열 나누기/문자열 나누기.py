def solution(s):
    i = na = nb = 0
    answer = 0
    for j in range(len(s)) :
        if len(s[j:]) == 1 :
            answer += 1
            break
        
        l = s[i] #기준 : b
        if s[j] == l : #b==b
            na += 1
            if na == nb :
                i = j+1
                answer += 1
            
        else : 
            nb += 1
            if na == nb :
                i = j+1
                answer += 1
    return answer         