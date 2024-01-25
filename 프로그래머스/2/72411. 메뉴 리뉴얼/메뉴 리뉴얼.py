def solution(orders, course):
    answer = []
    for i in range(len(orders)) :
        dd = sorted(orders[i])
        ddd = ''.join(sorted(dd))
        orders[i]=ddd

    from itertools import combinations, permutations
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
        
        c_list = sorted(c_dict.items(), key=lambda x: x[1], reverse=True)
        
        if c_list and c_list[0][1] >= 2 :
            answer.append(c_list[0][0])
        else :
            continue
        k = 1
        while len(c_list)>=k+1 and c_list[k][1] == c_list[0][1] :
            answer.append(c_list[k][0])
            k += 1
            
    answer.sort()      
    return answer