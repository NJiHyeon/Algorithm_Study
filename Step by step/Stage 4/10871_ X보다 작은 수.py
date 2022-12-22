# 배열을 입력받고 X보다 작은 수를 찾는 문제
N, X = map(int, input().split())
A = list(map(int, input().split()))


for i in range(1, N) :
    if A[i] < X : 
        print(A[i], end= " ")
