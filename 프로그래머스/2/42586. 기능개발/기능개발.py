def solution(progresses, speeds):
    import math
    days = []
    for i in range(len(progresses)) :
        days.append(math.ceil((100-progresses[i])/speeds[i]))

    answer = []
    stack = []
    for d in days :
        if len(stack) == 0 :
            stack.append(d)
        else :
            if stack[0] >= d :
                stack.append(d)
            elif stack[0] < d :
                answer.append(len(stack))
                stack.clear()
                stack.append(d)
            
    answer.append(len(stack))
    return answer
