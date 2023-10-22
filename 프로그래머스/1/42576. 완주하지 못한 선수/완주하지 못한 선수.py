def solution(participant, completion):
    l = list(set(participant)-set(completion))
    if len(l) == 0 :
        answer = [x for x,y in zip(sorted(participant), sorted(completion)) if x != y]
    else :
        answer = l
    return answer[0]