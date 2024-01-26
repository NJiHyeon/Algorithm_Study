def solution(book_time):
    from collections import deque
    answer = 1
    book_time.sort()
    t = book_time.pop(0)
    new_t = ''
    while book_time :
        for i in range(len(book_time)) :
            if plus(t) <= book_time[i][0] :
                new_t = book_time[i]
                book_time.pop(i)
                break
        if new_t != '' :
            t = new_t
            new_t = ''
        else :
            t = book_time.pop(0)
            answer += 1
    return answer
    
    
def plus(t) :
    if int(t[1][3:]) + 10 < 60 :
        enter = t[1][:2] + ':' + str(int(t[1][3:])+10)
    else :
        h = str(int(t[1][:2]) + 1)
        m = str(int(t[1][3:]) + 10 - 60)
        enter = '0'*(2-len(h)) + h + ':' + '0'*(2-len(m)) + m
    return enter