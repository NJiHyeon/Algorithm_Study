def solution(new_id):
    answer = ''
    # 1단계
    id = new_id
    id = id.lower()
    
    # 2단계
    for i in id :
        if i.isdigit() or i.islower() or i in ['-', '_', '.'] :
            answer += i
    # 3단계
    while '..' in answer :
        answer = answer.replace('..', '.')
        
    # 4단계
    if answer[0] == '.' :
        answer = answer[1:]
    if len(answer)>0 and answer[-1] == '.' :
        answer = answer[:-1]
        
    # 5단계
    if answer == '' :
        answer = 'a'
        
    # 6단계
    if len(answer) >= 16 :
        answer = answer[:15]
    if answer[-1] == '.' :
        answer = answer[:-1]
        
    # 7단계
    if len(answer) <= 2 :
        l = len(answer)
        while True :
            answer += answer[-1]
            l += 1
            if l == 3 :
                break
    
    return answer