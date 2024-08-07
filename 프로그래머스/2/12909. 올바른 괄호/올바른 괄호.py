def solution(s) :
    stack = []
    for ss in s :
        if ss=="(" :
            stack.append(ss)
        else :
            if stack :
                stack.pop()
            else :
                return False
    if stack :
        return False
    return True



# 시간초과 코드,,
'''
def solution(s):
    while "()" in s :
        s = s.replace("()", "")
    return True if s=="" else False
'''