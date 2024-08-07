def solution(n):
    b = n #n부터 시작
    while True :
        n_2 = bin(n)[2:]
        b += 1 #1씩 증가
        big_2 = bin(b)[2:]
        if n_2.count('1') == big_2.count('1') :
            break
    return b