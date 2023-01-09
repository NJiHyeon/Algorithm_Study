# 각 문자를 반복하여 출력하는 문제 (틀림)
T = int(input())
for i in range(T) :
        N, C = input().split()
        for i in range(0, len(C)) :
            print(C[i]*int(N), end='')
        print() ## 중요중요

        