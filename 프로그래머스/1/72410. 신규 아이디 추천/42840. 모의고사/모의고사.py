def solution(answers):
    n = len(answers)
    A1 = [1, 2, 3, 4, 5]
    a1 = [1, 2, 3, 4, 5] * (n//5) + A1[0:n%5]
    A2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] * (n//8) + A2[0:n%8]
    A3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (n//10) + A3[0:n%10]
    
    s1 = s2 = s3 = 0
    
    for i in range(len(answers)) :
        if a1[i] == answers[i] :
            s1 += 1
    
    for i in range(len(answers)) :
        if a2[i] == answers[i] :
            s2 += 1
    
    for i in range(len(answers)) :
        if a3[i] == answers[i] :
            s3 += 1
    
    

    score = []
    score.append(s1)
    score.append(s2)
    score.append(s3)
    m = max(score)
    
    r = []
    for j in range(3) :
        if score[j] == m :
            r.append(j+1)
            
    return r