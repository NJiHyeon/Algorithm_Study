def solution(n, t, m, p):
    answer = '0'
    i = 0
    while True :
        i += 1
        answer += jinsu(i, n)
        if len(answer) >= (m*t) :
            break
    real = ''
    for i in range(p-1, len(answer), m) :
        real += answer[i]
        if len(real) == t :
            return real
        


def jinsu(n, k) :
    rev_base = ''
    while n > 0 :
        n, mod = divmod(n, k)
        if mod == 10 :
            mod = 'A'
        elif mod == 11 :
            mod = 'B'
        elif mod == 12 :
            mod = 'C'
        elif mod == 13 :
            mod = 'D'
        elif mod == 14 :
            mod = 'E'
        elif mod == 15 :
            mod = 'F'
        rev_base += str(mod)
    return rev_base[::-1]