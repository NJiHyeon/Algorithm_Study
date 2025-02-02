def solution(orders, course):
    # 단품 메뉴들을 조합해서 코스요리 형태로 재구성하기 
    # 메뉴 주문시 가장 많이 함께 주문한 단품메뉴들을 선택
    # 단, 최소 2가지 이상의 단품메뉴로 구성 / 최소 2명 이상의 손님으로부터 주문된 것 단품메뉴 조합에 대해서만 후보에 포함 
    
    # 'XA'와 'AX'가 다르게 카운트 되는 것 방지 
    for i in range(len(orders)):
        orders[i] = ''.join(sorted(list(orders[i])))
    
    def make_combi(orders, n):
        combi = []
        def backtrack(order, cur, cur_i, n):
            # base case
            if len(cur) == n:
                combi.append(''.join(cur))
                return
            # repeat
            for i in range(cur_i, len(order)):
                if order[i] not in cur:
                    cur.append(order[i])
                    backtrack(order, cur, i+1, n)
                    cur.pop()
            
        for order in orders:
            backtrack(order, [], 0, n)
        return combi
    
    result = []
    for n in course:
        max_n = 0
        combi = make_combi(orders, n)
        dict = {}
        for f in combi:
            if f not in dict:
                dict[f] = 1
            else:
                dict[f] += 1
            max_n = max(max_n, dict[f])
        for k, v in dict.items():
            if v >= 2 and v == max_n:
                result.append(k)
    result.sort()
    return result