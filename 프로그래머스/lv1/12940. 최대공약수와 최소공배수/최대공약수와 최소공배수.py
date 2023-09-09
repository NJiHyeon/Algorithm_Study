def solution(n, m):
    answer = []
    answer.append(GCD(n,m))
    answer.append(LCM(n, m))
    return answer

# 최대공약수
def GCD(n, m) :
    while(m) :
        n, m = m, n%m
    return n
    
# 최소공배수
def LCM(n, m) :
    return (n*m)//GCD(n,m)
    