def solution(s, n):
    u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = ''
    for i in range(len(s)) :
        if s[i].isupper() :
            j = u.index(s[i])
            if j+n > 25 :
                j -= 26
            answer += u[j+n]
        elif s[i].islower() :
            j = l.index(s[i])
            if j+n > 25 :
                j -= 26
            answer += l[j+n]
        elif s[i] == ' ' :
            answer += ' '
    return answer