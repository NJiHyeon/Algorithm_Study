# 2차원 배열을 활용하여 색종이로 평면을 덮는 문제
"""
좌측 하단의 좌표를 받아 가로와 세로의 길이가 10인 사각형을 1로 표현한다.
결국, 겹치는 부분들도 모두 1로 표현 될 것이고, 결국엔 2차원 리스트에서 1의 개수를 구하면 되는 문제
(겹치는 넓이를 빼려고 시도하면 엄청 복잡해짐 ! 넓이가 아니라 개수로 생각하자)
"""
#-------------------------------------------------------------------------------
t = int(input())
white = [[0]*100 for _ in range(100)]
for _ in range(t) :
    a, b = map(int, input().split())
    for i in range(a, a+10) :
        for j in range(b, b+10) :
            white[i][j] = 1
            
result = 0
for k in range(100) :
    result += white[k].count(1)
        
print(result)
            