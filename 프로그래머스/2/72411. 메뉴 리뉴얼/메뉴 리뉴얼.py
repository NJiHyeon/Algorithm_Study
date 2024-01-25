def solution(orders, course):
    answer = []
    # 조건 : 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬
    for i in range(len(orders)) :
        dd = sorted(orders[i])
        ddd = ''.join(sorted(dd))
        orders[i]=ddd

    from itertools import combinations
    for c in course :
        c_dict = dict()
        for i in range(len(orders)) :
            if len(orders[i]) >= c :
                combi = list(combinations(orders[i], c))
                for com in combi :
                    name = ''.join(com)
                    if name in c_dict :
                        c_dict[name] += 1
                    else :
                        c_dict[name] = 1
        
        # 제일 많은 순으로 
        c_list = sorted(c_dict.items(), key=lambda x: x[1], reverse=True)
        
        # 조건 : 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합 (앞에서 정렬했으므로 첫번째 인덱스 확인)
        if c_list and c_list[0][1] >= 2 :
            answer.append(c_list[0][0])
        else :
            continue
        # 조건 : 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
        k = 1
        while len(c_list)>=k+1 and c_list[k][1] == c_list[0][1] :
            answer.append(c_list[k][0])
            k += 1
    # 조건 : 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순      
    answer.sort()      
    return answer