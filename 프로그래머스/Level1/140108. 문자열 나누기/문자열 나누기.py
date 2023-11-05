def solution(s):
    i = na = nb = 0
    answer = 0 # 출력값
    for j in range(len(s)) :
        if len(s[j:]) == 1 : # 마지막번째 문자면 answer에 1 더하고 끝.
            answer += 1
            break
        
        l = s[i] #기준정하기
        
        if s[j] == l : 
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