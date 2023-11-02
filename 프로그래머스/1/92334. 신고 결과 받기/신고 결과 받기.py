def solution(id_list, report, k):
    # a유저가 b유저를 여러번 신고할 경우 신고횟수가 1번으로 처리되므로 report에서 report[i]와 report[j]가 같을 경우 제거
    report = set(report)
    
    # 유저의 신고받은 횟수 세기 
    sin = {user:0 for user in id_list} #초기화
    for r in report :
        o = r.split(" ") 
        sin[o[1]] += 1
    
    # 신고한 유저가 메일을 받을 횟수
    mail = {user:0 for user in id_list} #초기화
    for id in id_list : 
        for s in sin : 
            # 조건
            '''
            1. id_list, sin 둘다를 도는 거니까 user가 겹칠수 있음 -> 자기가 자신을 신고한 꼴 -> 신고한 사람(id)랑 신고받은 사람(s)가 달라야 함
            2. 신고받은 횟수가 k이상이어야 함
            3. report를 참고하여 id(user)가 k이상 신고를 받은 user를 신고했어야 함.
            '''
            if sin[s] >= k and (id!=s) and ((id+" "+s) in report) :
                mail[id] += 1
    return list(mail.values())