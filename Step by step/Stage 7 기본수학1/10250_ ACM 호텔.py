# 호텔 방 번호의 규칙을 찾아 출력하는 문제
t = int(input())

for _ in range(t) :
    H, W, N = map(int, input().split())
    l = N % H
    h = N // H + 1
    if N % H == 0 :
        h = N//H
        l = H
    print(l*100+h)