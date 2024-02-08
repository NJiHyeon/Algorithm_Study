def solution(p):
    if p == '' :
        return p
    else :
        u, v = make_str(p)
        if correct_str(u) == True :
            u += solution(v)
            return u
        else :
            new = '('
            new += solution(v)
            new += ')'
            u = u[1:-1]
            for uu in u :
                if uu == '(' :
                    new += ')'
                else :
                    new += '('
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