def solution(order) :
    answer = 0
    cont = []
    n = 1
    while n != len(order)+1 :
        cont.append(n)
        while cont[-1]==order[answer] :
            answer += 1
            cont.pop()
            if len(cont) == 0 :
                break
        n += 1
    return answer
    

        