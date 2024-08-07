def solution(participant, completion):
    participant.sort()
    completion.sort()
    n = []
    for i in range(len(completion)) :
        if participant[i]!=completion[i] :
            n.append(participant[i])
            
    if len(n)==0 :
        return participant[-1]
    else :
        return n[0]