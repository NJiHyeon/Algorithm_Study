def solution(fees, records):
    answer = []
    car = {}
    for i in range(len(records)) :
        if records[i][6:10] in car :
            car[records[i][6:10]].append(records[i][0:5])
        else :
            car[records[i][6:10]] = [records[i][0:5]]
    car = dict(sorted(car.items(), reverse=False))
    for c in car :
        if len(car[c]) % 2 == 1 :
            car[c].append('23:59')
        time = 0    
        for t in range(0, len(car[c])-1, 2) :
            time += cal(car[c][t+1], car[c][t])
        won = cal2(time, fees)
        answer.append(won)
    return answer

# "07:59", "05:34"
def cal(b, s) :
    if b[3:] >= s[3:] :
        h = int(b[0:2]) - int(s[0:2])
        m = int(b[3:]) - int(s[3:])
        total = h*60+m
    else :
        h = int(b[0:2]) - int(s[0:2]) - 1
        m = 60 + int(b[3:]) - int(s[3:])
        total = h*60+m
    return total
    
def cal2(time, fees) :
    import numpy as np
    if time <= fees[0] :
        return fees[1]
    else :
        return fees[1] + np.ceil(((time-fees[0])/fees[2]))*fees[3]
        