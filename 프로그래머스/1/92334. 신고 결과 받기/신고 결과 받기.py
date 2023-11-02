def solution(id_list, report, k):
    # a유저가 b유저를 여러번 신고할 경우 신고횟수가 1번으로 처리되므로 report에서 report[i]와 report[j]가 같을 경우 제거
    report = set(report)
    
    # 유저의 신고받은 횟수 세기 
    sin = {user:0 for user in id_list}
    for r in report :
        o = r.split(" ") 
        sin[o[1]] += 1
        
    mail = {user:0 for user in id_list}
    for id in id_list : 
        for s in sin : 
            if sin[s] >= k and (id!=s) and ((id+" "+s) in report) :
                mail[id] += 1
    return list(mail.values())