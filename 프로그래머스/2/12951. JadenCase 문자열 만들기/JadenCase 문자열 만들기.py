def solution(s):
    answer = ''
    for i in range(len(s)) :
        if i==0 :
            answer += s[i].upper()
        elif s[i].isalnum() and s[i-1]==' ' :
            answer += s[i].upper()
        elif s[i].isalnum() and s[i-1]!=' ' :
            answer += s[i].lower()
        else :
            answer += s[i]
    return answer