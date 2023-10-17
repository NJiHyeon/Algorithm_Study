def solution(nums):
    answer = 0
    pon = list(set(nums))
    n = len(nums)//2
    i = 0
    while True :
        if i<n and len(pon) > 0 :
            answer += 1
            i += 1
            pon.pop(-1)
            
        elif i<n  :
            answer += 0
            i += 1
        else :
            break
    
    return answer