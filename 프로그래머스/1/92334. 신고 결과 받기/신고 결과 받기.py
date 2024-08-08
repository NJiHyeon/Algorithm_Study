def solution(id_list, report, k):
    # id_list = ["muzi", "frodo", "apeach", "neo"]
    # report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    # k = 2
    report_dict = {id_list[i] : set() for i in range(len(id_list))}
    singo_dict = {}

    for i in range(len(report)):
        li = report[i].split(' ')
        a, b = li[0], li[1]
        if b in report_dict[a]:
            pass
        else:
            report_dict[a].add(b)
            if b not in singo_dict:
                singo_dict[b] = 1
            else:
                singo_dict[b] += 1
            
    result = []
    for id in id_list:
        # muzi
        mail = 0
        singo_id_list = report_dict[id] #["frodo", "neo"]
        if singo_id_list:
            for singo_id in singo_id_list:
                if singo_dict[singo_id] >= k:
                    mail += 1
        result.append(mail)
        
    return result
        
        
        