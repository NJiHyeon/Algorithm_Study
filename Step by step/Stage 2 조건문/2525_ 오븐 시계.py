# 틀림 ㅠ
A, B = map(int, input().split())
C = int(input())
h = (B+C)//60
m = (B+C)%60
if B+C < 60 :
    print(A, B+C)
elif 60 <= B+C :
    if (A+h) < 23 :
        print(A+h, m)
    else :
        print(A+h-24, m)
            
# 정답                     
H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)