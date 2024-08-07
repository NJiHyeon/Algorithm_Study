def solution(storey):
    answer = 0
    while storey :
        r = storey % 10
        if 0 <= r <= 4 :
            answer += r
        elif 6 <= r <= 9 :
            answer += (10-r)
            storey += 10
        else :
            if (storey//10) % 10 > 4 :
                storey += 10
            answer += r
        storey //= 10
    return answer