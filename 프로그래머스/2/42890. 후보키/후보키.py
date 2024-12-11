def solution(relation):
    combi = []
    category = [str(i) for i in range(len(relation[0]))]
    def backtrack(cur, cur_i, n):
        if len(cur) == n:
            combi.append(cur[:])
        for i in range(cur_i, len(relation[0])):
            cur.append(category[i])
            backtrack(cur, i+1, n)
            cur.pop()
    for n in range(1, len(relation[0])+1):
        backtrack([], 0, n)

    # 테이블 만들기 (딕셔너리로 구성)
    candidate_key = {}
    for i in range(len(relation)):
        for j in range(len(relation[0])):
            if str(j) not in candidate_key:
                candidate_key[str(j)] = [relation[i][j]]
            else:
                candidate_key[str(j)].append(relation[i][j])

    # 유일성+최소성 판단
    output = []
    for cur_cate in combi:
        # 유일성
        curr = []
        for i in range(len(relation)):
            k = ''
            for c in cur_cate:
                k += candidate_key[c][i]
            curr.append(k)
        if len(curr) != len(list(set(curr))):
            continue
        # 최소성
        mini = 'Y'
        for o in output:
            if set(o).issubset(set(cur_cate)):
                mini = 'N'
                break
        if mini == 'Y':
            output.append(cur_cate)
    return len(output)