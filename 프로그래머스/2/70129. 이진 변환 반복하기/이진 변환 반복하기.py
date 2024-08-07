def solution(s):
    answer = []
    while True :
        if s == '1' :
            break
        else :
            # 제거할 0의 개수
            n = s.count('0')
            answer.append(n)
            # 0 제거 후 길이
            l = len(s) - n
            # 다시 이진 변환
            s = bin(l)[2:]
    return [len(answer), sum(answer)]