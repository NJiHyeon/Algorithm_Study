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
            '''
            # 3이 있을 때 3이 들어올 때
            if stack[0] == stack[-1] == d :
                answer.append(1)
                stack.pop()
                stack.append(d)
            # 10, 3이 있을 때 3이 들어올 때
            elif (stack[0]!=stack[-1]) and (stack[-1]==d) :
                stack.append(d)
            if stack[-1] >= d :
                stack.append(d)
            # 10이 있을 때 3이 들어올 때
            elif stack[-1] > d :
                stack.append(d)
            '''
            if stack[0] >= d :
                stack.append(d)
            # 10이 있을 때 12가 들어올 때
            elif stack[0] < d :
                answer.append(len(stack))
                stack.clear()
                stack.append(d)
            
    answer.append(len(stack))
    return answer