def solution(s):
    answer = []
    for i in range(len(s)) :
        if s[i] in s[:i] :
            new_s = s[:i]
            reverse_s = new_s[::-1]
            answer.append(reverse_s.index(s[i]) + 1)
        else :
            answer.append(-1)  
    return answer


