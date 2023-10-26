def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for sk in skip :
        alpha = alpha.replace(sk, "")
    for a in s :
        answer += alpha[(alpha.find(a)+index)%len(alpha)]
    return answer