# 최댓값이 어디에 있는지 찾는 문제 -> 틀림( 복습 )
# Input
    # 3
    # 29
    # 38
    # 12
    # 57
    # 74
    # 40
    # 85
    # 61
# Output
    # 85
    # 8
    
n = []
for i in range(9) :
    N = int(input())
    n.append(N)
print(max(n))
print(n.index(max(n))+1)
