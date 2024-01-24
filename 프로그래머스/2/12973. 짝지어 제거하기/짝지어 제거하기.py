def solution(s):
    stack = []
    for t in s :
        if stack and stack[-1] == t :
            stack.pop()
        else :
            stack.append(t)
    
    if len(stack) == 0 :
        return 1
    else :
        return 0