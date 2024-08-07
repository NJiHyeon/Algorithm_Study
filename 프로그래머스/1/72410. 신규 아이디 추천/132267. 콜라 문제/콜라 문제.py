def solution(a, b, n):
    answer = 0 # 총 콜라병을 받는 개수
    # 남은 콜라병이 마트에 주어야할 개수 (a)보다 작으면 끝
    while True :
        take = n // a * b # 마트에서 콜라병을 받는 개수
        answer += take   # 최종 개수에 더하기
        remain = n % a # 나누어 떨어지지 않고 그대로 집에 가져오는 콜라병의 개수
        n = take + remain 
        if n < a : 
            break
        
    return answer