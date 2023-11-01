def solution(today, terms, privacies):
    answer = []
    trash_list = []
    
    for i in range(len(privacies)) :
        for t in terms :
            if t[0] in privacies[i] : 
                trash_month = int(t[2:]) + int(privacies[i][5:7]) 
                # 더했을때 12월의 배수이면 조심해야함 !
                if trash_month%12==0 :
                    new_month = 12
                    new_year = int(privacies[i][:4]) + (trash_month // 12) - 1
                else :
                    new_month = trash_month % 12 
                    new_year = int(privacies[i][:4]) + (trash_month // 12) 
                trash_day = ''
                if len(str(new_month))==1 :
                    trash_day = str(new_year)+'.0'+str(new_month)+'.'+privacies[i][8:10]
                else :
                    trash_day = str(new_year)+'.'+str(new_month)+'.'+privacies[i][8:10]

                trash_list.append(trash_day)

    
    today = int(today.replace('.', ''))
    for j in range(len(trash_list)) : 
        k = int(trash_list[j].replace('.', ''))
        if today >= k :
            answer.append(j+1)
    
    return answer