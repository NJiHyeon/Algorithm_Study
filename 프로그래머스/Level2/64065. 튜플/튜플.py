def solution(s):
    s = s[2:-2].split('},{')
    s = sorted(s, key=lambda x : len(x))
    answer = []
    for ss in s :
        ss = list(map(int, ss.split(',')))
        for i in ss :
            if i not in answer :
                answer.append(i)
    return answer

'''
def solutions(s) :
    import collections
    answer = []
    s = s[1:-1]
    i = 0
    dig = ''
    while True :
        if i == len(s) :
            break

        if s[i].isdigit() :
            dig += s[i]
        else :
            if dig.isdigit() :
                answer.append(int(dig))
            dig = ''
        i += 1
'''