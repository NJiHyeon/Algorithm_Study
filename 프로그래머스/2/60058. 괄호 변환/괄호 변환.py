def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if p == '' :
        return p
    # 2. 그렇지 않은 경우~
    else :
        # 2. w를 u,v로 분리 (단, u는 "균형잡힌 문자열")
        u, v = make_str(p)
        # 3. 문자열 u가 "올바른 문자열"인 경우, v에 대해 다시 수행
        if correct_str(u) == True :
            # 3-1. 수행한 결과 문자열은 u에 이어 붙인 후 반환
            u += solution(v)
            return u
        # 4. u가 "올바른 문자열"이 아닌 경우
        else :
            # 4-1. 빈 문자열에 '(' 붙이기
            new = '('
            # 4-2. 문자열 v에 대해 다시 수행한 결과를 이어 붙이기
            new += solution(v)
            # 4-3. ')'를 다시 붙이기
            new += ')'
            # 4-4. u의 첫번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집에서 뒤에 붙이기
            u = u[1:-1]
            for uu in u :
                if uu == '(' :
                    new += ')'
                else :
                    new += '('
            # 4-5. 생성된 문자열을 반환
            return new
        
def make_str(p) :
    a, b = 0, 0
    for pp in p :
        if pp == "(" :
            a += 1
        else :
            b += 1
        if a==b :
            i = a+b
            u = p[:i]
            v = p[i:]
            return u,v
    
def correct_str(s):
	stack=[]
	stack.append(s[0])
	for i in range(1,len(s)):
		if len(stack)==0 or stack[-1]==')' or (stack[-1]=='(' and s[i]=='('):
			stack.append(s[i])
		else:
			stack.pop()
	if len(stack)==0: return True
	else: return False