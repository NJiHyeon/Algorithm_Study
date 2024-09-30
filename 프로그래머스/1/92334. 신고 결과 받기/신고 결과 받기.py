def solution(id_list, report, k):
    result = []
    talking = {id:[] for id in id_list}
    talked = {id:0 for id in id_list}
    for tmp in report:
        ing, ed = tmp.split(" ")[0], tmp.split(" ")[1]
        if ed in talking[ing]:
            pass
        else:
            talking[ing].append(ed)
            talked[ed] += 1
    
    for id in id_list:
        n = 0
        for ed in talking[id]:
            if talked[ed] >= k:
                n += 1
        result.append(n)
    return result
            
        