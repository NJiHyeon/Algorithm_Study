def solution(dartResult):
    result = []
    score = 0
    dartResult = dartResult.replace('10', 't')
    
    for i in dartResult :
        if i.isnumeric() :
            score += int(i)
            continue # 초기화 X
        elif i=='t' :
            score += 10 
            continue # 초기화 X
            
        elif i=='S' :
            result.append(score)
        elif i=='D' :
            result.append(score**2)
        elif i=='T' :
            result.append(score**3)
            
        elif i=='*' :
            if len(result)>1 : # 한판이상
                result[-1] *= 2
                result[-2] *= 2
            else : #한판
                result[-1] *= 2
        elif i=='#' :
            result[-1] *= -1
            
        score = 0 # 한판점수 초기화
        
    return sum(result)