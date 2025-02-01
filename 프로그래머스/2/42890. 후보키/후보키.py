def solution(relation):
    col = 'ABCDEFGH'
    dict = {col[i]:i for i in range(len(relation[0]))}
    candidate_key = []
    
    # 1. 조합 만들기
    combi = []
    def backtrack(cur, cur_i, n):
        if len(cur) == n:
            combi.append(''.join(cur[:]))
            return
        for i in range(cur_i, len(relation[0])):
            cur.append(col[i])
            backtrack(cur, i+1, n)
            cur.pop()
    for n in range(1, len(relation[0])+1):
        backtrack([], 0, n)
    
    # 2. 최소성 확인
    for new_key in combi:
        uniq = []
        mini = True
        for cand in candidate_key:
            if set(cand).issubset(set(new_key)):
                mini = False
        # 3. 유일성 확인
        if mini == True:
            for r in range(len(relation)):
                p = ''
                for c in new_key:
                    p += relation[r][dict[c]]
                uniq.append(p)
            if len(list(set(uniq))) == len(uniq):
                candidate_key.append(new_key)
    return len(candidate_key)
    