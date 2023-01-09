# 내가 제출한 방법
A, B, C, D, E, F = input().split()
print(1-int(A), 1-int(B), 2-int(C), 2-int(D), 2-int(E), 8-int(F))

# 다른 방법(중요..)
cp = [1, 1, 2, 2, 2, 8]
li = list(map(int, input().split()))
for i in range(6):
    print(cp[i]-li[i],end=' ')