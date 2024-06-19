def solution(expression):
    from itertools import permutations
    answer = []
    buho = {}
    bh = []
    bh_p = []
    if '+' in expression :
        l = expression.count('+')
        buho['+'] = l
        bh.append('+')
    if '-' in expression :
        l = expression.count('-')
        buho['-'] = l
        bh.append('-')
    if '*' in expression :
        l = expression.count('*')
        buho['*'] = l
        bh.append('*')
    bh_l = len(bh)
    for p in permutations(bh, bh_l) :
        bh_p.append(p)
    
    for b in bh_p :
        expression_list = make_list(expression)
        buho_d = buho.copy()
        won = make_won(expression_list, b, buho_d)
        answer.append(abs(int(won)))
    return max(answer)
    
def make_list(expression) :
    m = []
    ep = ''
    for e in expression :
        if e == '-' :
            m.append(ep)
            m.append(e)
            ep = ''
        elif e == '+' :
            m.append(ep)
            m.append(e)
            ep = ''
        elif e == '*' :
            m.append(ep)
            m.append(e)
            ep = ''
        else :
            ep += e
    m.append(ep)
    return m
    
def make_won(expression_list, b, buho) :
    for bb in b :
        while buho[bb] > 0 :
            buho[bb] -= 1
            i = expression_list.index(bb)
            if bb == '+' :
                c = int(expression_list[i-1]) + int(expression_list[i+1])
            elif bb == '-' :
                c = int(expression_list[i-1]) - int(expression_list[i+1])
            elif bb == '*' :
                c = int(expression_list[i-1]) * int(expression_list[i+1])
            expression_list[i-1] = c
            del expression_list[i:i+2]
    return expression_list[0]