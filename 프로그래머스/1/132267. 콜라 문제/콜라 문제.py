def solution(a, b, n):
    answer = 0
    while True :
        take = n // a * b # 6
        answer += take   # 6
        
        remain = n % a # 2
        
        n = take + remain
        
        if n < a : 
            break
        
        
    return answer