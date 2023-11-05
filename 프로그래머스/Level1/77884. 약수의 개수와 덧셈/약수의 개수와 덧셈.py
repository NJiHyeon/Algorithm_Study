def solution(left, right):
    answer = 0
    for n in range(left, right+1) :
        # 약수의 개수
        divisor = 0
        for i in range(1, n+1) :
            if n%i == 0 :
                divisor += 1
        # 홀/짝 확인 후 더하고 뺄지
        if divisor%2 == 0:
            answer += n
        else :
            answer -= n
    
    return answer