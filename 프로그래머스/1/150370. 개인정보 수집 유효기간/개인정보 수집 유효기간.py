def solution(today, terms, privacies):
    result = []
    terms_dict = {}
    for term in terms:
        term_ = term.split(" ")
        terms_dict[term_[0]] = int(term_[1])

    def cal(tmp, select):
        if select == 'p':
            ymd, t = tmp.split(" ")[0], tmp.split(" ")[1]
            y, m, d = int(ymd.split(".")[0]), int(ymd.split(".")[1]), int(ymd.split(".")[2])
            m += terms_dict[t]
            day_cal = (y-2000)*336 + m*28 + d
        else:
            ymd = tmp.split(".")
            y, m, d = int(ymd[0]), int(ymd[1]), int(ymd[2])
            day_cal = (y-2000)*336 + m*28 + d
        return day_cal
            
    today_cal = cal(today, 't')
    for i, privacy in enumerate(privacies):
        cur_cal = cal(privacy, 'p')
        if (today_cal - cur_cal) >= 0:
            result.append(i+1)
    return result
    
    