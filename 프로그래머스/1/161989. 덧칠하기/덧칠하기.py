def solution(n, m, section):
    answer = 1 #section[i]-start의 값이 m보다 작으면 한번만 칠하면 끝나는 거니까 1로 설정
    start = section[0] 
    for i in range(1, len(section)) : #section list 돌기
        if section[i]-start >= m : #거리가 m이상이면 롤러 한번으로 안됨
            answer += 1 #롤러 횟수 +1
            start = section[i] #시작점 변경
            
    return answer
    
    

    