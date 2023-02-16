# 수 대신 문자열을 저장하는 문제
# -----------------------------------------------------------------------------
import sys
N, M = map(int, sys.stdin.readline().split())
S = []
for i in range(N) :
    s = input()
    S.append(s)
    
n = 0
for j in range(M) :
    c = input()
    if c in S :
        n += 1
    else : 
        n = n
print(n)

# ----------------------------------------------------------
## for문 한번에 묶기 ⭕
import sys
N, M = map(int, sys.stdin.readline().split())
S = []
n = 0
for i in range(N+M) :
    if i < N :
        s = input()
        S.append(s)
    else : 
        c = input()
        if c in S :
            n += 1
        else : 
            n = n
            
print(n)