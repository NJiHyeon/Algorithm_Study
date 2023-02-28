"""
반복적인 규칙 찾는 문제
어려운 문제는 아니지만 주의해야 하는 문제
"""
# 호텔 방 번호의 규칙을 찾아 출력하는 문제
t = int(input())
for _ in range(t) :
    H, W, N = map(int, input().split())
    if N % H == 0 :
        h = N//H
        l = H
    
    else : 
        l = N % H
        h = N // H + 1

    print(l*100+h)