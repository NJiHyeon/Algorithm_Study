def solution(n):
    answer = 1
    for i in range(1, n//2 + 1) : #시작점
        total = 0
        while n>total :
            total += i
            if total == n :
                answer += 1
                break
            i+=1   
    return answer