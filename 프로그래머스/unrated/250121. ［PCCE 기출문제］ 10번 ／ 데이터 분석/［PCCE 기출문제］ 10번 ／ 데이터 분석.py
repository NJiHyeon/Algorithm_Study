def solution(data, ext, val_ext, sort_by):
    answer = []
    sub = ['code', 'date', 'maximum', 'remain']
    
    select = sub.index(ext)
    sort = sub.index(sort_by)
    for i in range(len(data)) :
        if data[i][select] < val_ext :
            answer.append(data[i])
    
    answer.sort(key=lambda x:x[sort])
    return answer
