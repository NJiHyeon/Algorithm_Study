def solution(s):
    reverse_s = sorted(s)
    answer=''
    for i in reverse_s[::-1] :
        answer+=i
    return answer