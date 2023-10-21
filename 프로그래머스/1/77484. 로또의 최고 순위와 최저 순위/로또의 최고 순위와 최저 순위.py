def solution(lottos, win_nums):
    answer = []
    result = 0
    d = lottos.count(0)
    
    for l in lottos :
        if l in win_nums :
            result += 1
    
    if result == 6 :
        answer = [1, 1]
    elif 1<=result<=5 :
        answer.append(7-result-d)
        answer.append(7-result)
    else :
        if 0<=d<=1 :
            answer.append(6)
            answer.append(6)
        else :
            answer.append(7-d)
            answer.append(6)
    
    return answer