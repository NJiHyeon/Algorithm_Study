def solution(n):
    answer = 1
    while n > answer :
        if n%answer == 1 :
            return answer
        else :
            answer += 1