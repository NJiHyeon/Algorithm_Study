def solution(today, terms, privacies):
    result = []
    terms_dict = {term.split(' ')[0] : int(term.split(' ')[1]) for term in terms}
    for i in range(len(privacies)):
        start_day, m = privacies[i].split(' ')[0], terms_dict[privacies[i].split(' ')[1]]
        
        # 날짜 계산
        start_y = int(start_day.split('.')[0])
        start_m = int(start_day.split('.')[1]) + m
        start_d = int(start_day.split('.')[2]) - 1
        
        if start_m > 12:
            if start_m % 12 != 0:
                start_y += (start_m // 12)
                start_m = (start_m % 12)
            else:
                start_y += (start_m // 12 - 1)
                start_m = 12
        
        if start_d == 0:
            start_d = 28
            start_m -= 1
            if start_m == 0:
                start_m = 12
                start_y -= 1

        
        # 자릿수
        if len(str(start_m)) == 1:
            start_m = f'0{start_m}'
        if len(str(start_d)) == 1:
            start_d = f'0{start_d}'
        
        end_day = f'{start_y}.{start_m}.{start_d}'
    
        if today > end_day:
            result.append(i+1)
    return result