# 내가 푼 방법
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

def cal() : 
    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)

cal()

# 다른 풀이
A,B,C = map(int,input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')