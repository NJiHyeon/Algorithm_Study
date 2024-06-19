def solution(p) :
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if p == '' :
        return p
    # 2. 문자열 w를 두 '균형잡힌 괄호 문자열' u, v로 분리한다. (단, u는 '균형잡힌 괄호 문자열'로 더이상 분리할 수 없어야 한다.)
    u, v = balanced_str(p)
    # 3. u가 '올바른 괄호 문자열'이라면 문자열 v에 대해 다시 1단계부터 수행 (수행한 결과 문자열을 u에 이어 붙인 후 반환)
    if correct_str(u) == True :
        u += solution(v)
        return u
    # 4. u가 '올바른 괄호 문자열'이 아니라면 아래 과정을 수행한다.
    else :
        # 4-1. 빈 문자열에 '(' 붙이기 
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙이기
        # 4-3. ')'를 다시 붙이기
        new_str = '(' + solution(v) + ')'
        # 4-4. u의 첫번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집기
        u = u[1:-1]
        for uu in u :
            if uu == '(' :
                new_str += ')'
            else :
                new_str += '('
        return new_str

def balanced_str(p) :
    # 균형잡힌 괄호 문자열로 분리하기
    a, b = 0, 0
    for pp in p :
        if pp == '(' :
            a += 1
        else :
            b += 1
        if a==b :
            u = p[:a+b]
            v = p[a+b:]
            return u,v
    
def correct_str(s) :
    # 올바른 괄호 문자열인지 확인하기
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)) :
        if len(stack)==0 or stack[-1]==')' or (stack[-1]=='(' and s[i]=='('):
            stack.append(s[i])
        else :
            stack.pop()
    if len(stack) == 0 :
        return True
    else :
        return False