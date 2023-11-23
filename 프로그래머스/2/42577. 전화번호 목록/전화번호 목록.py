def solution(phone_book):
    answer = True
    for i in range(len(phone_book)) :
        s = phone_book[i]
        l = len(s)
        for j in range(len(phone_book)) :
            if s == phone_book[j][:l] and i!=j :
                return False
        
    return answer