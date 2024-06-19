def solution(order) :
    answer = 0
    n = 1 
    container = []
    while n != len(order)+1 :
        container.append(n)
        while order[answer] == container[-1] :
            answer += 1
            container.pop()
            if len(container)==0 :
                break
        n += 1
        
    return answer

        