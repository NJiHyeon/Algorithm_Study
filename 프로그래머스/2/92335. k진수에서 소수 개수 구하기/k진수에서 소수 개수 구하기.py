def solution(n, k):
    new = jinsu(n, k)
    ss_list = []
    ss = ''
    for s in new :
        if s!='0' :
            ss += s
        else :
            if ss!='':
                ss_list.append(ss)
                ss_list.append(s)
            else :
                ss_list.append(s)
            ss = ''
    if ss!='' :
        ss_list.append(ss)
    
    answer = 0
    for u in ss_list :
        if u!='1' and ('0' not in u) and (is_prime_number(int(u))) :
            answer += 1
    return answer


def jinsu(n, q) :
    rev_base = ''
    while n > 0 :
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]

def is_prime_number(x):
    import math
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
