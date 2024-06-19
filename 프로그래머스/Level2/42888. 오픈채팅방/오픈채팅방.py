def solution(record):
    answer = []
    record_ = record[::-1]
    name = dict()
    for r in record_ :
        r_list = r.split(" ")
        if (r_list[0]=="Change" or r_list[0]=="Enter") and (r_list[1] not in name) :
            name[r_list[1]] = r_list[2]
    
    for r in record :
        r_list = r.split(" ")
        if r_list[0] == "Enter" :
            exp = name[r_list[1]] + "님이 들어왔습니다."
            answer.append(exp)
        elif r_list[0] == "Leave" :
            exp = name[r_list[1]] + "님이 나갔습니다."
            answer.append(exp)
        
    return answer