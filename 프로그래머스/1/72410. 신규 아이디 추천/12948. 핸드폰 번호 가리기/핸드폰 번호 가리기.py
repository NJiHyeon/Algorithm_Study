def solution(phone_number):
    last = phone_number[-4:]
    change = len(phone_number)-4
    
    answer = '*'*change
    answer += str(last)
    return answer
    
    