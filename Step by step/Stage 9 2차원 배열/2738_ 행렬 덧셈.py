# 행렬을 2차원 배열로 만들어 더하는 문제
#------------------------------------------------------------------------------------- 
# My code (한꺼번에 담아서 출력)
N, M = map(int, input().split())
aa = []
for i in range(2) :
    for j in range(N) :
        numbers = list(map(int, input().split()))
        aa.append(numbers) 

for i in range(N) : 
    for j in range(M) :
        print(aa[i][j] + aa[i+N][j], end=' ')
    print()    

#-------------------------------------------------------------------------------------   
# Googling Code (두 행렬을 따로 만들어서 숫자를 담음)
A, B = [], []
N, M = map(int, input().split())
for row in range(N) :
    row = list(map(int, input().split()))
    A.append(row)
    
for row in range(N) :
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N) :
    for col in range(M) :
        print(A[row][col] + B[row][col], end=' ')
    print()