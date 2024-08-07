def solution(s):
    answer = ''
    s_split = s.split(' ')
    for s in s_split :
        for i in range(len(s)) :
            if i%2 == 0 :
                answer += s[i].upper()
            else :
                answer += s[i].lower()
        answer += ' '
    return answer[:-1]