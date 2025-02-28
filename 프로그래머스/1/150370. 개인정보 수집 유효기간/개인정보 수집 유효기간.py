def solution(today, terms, privacies):
    terms_dict = {term[0]:int(term[2:]) for term in terms}

    def yyyymmdd_to_dd(day, category=None):
        y, m, d = day.split('.')
        to_dd = (int(y)-2000)*12*28 + (int(m)-1)*28 + (int(d)-1)
        if category:
            to_dd += terms_dict[category]*28
        return to_dd
        
    result = []
    today = yyyymmdd_to_dd(today)
    for i in range(len(privacies)):
        start_day, category = privacies[i].split(" ")
        end_day = yyyymmdd_to_dd(start_day, category)
        if end_day <= today:
            result.append(i+1)
    return result