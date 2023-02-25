# 체스판을 만드는 모든 경우를 시도하여 최적의 방법을 찾는 문제 ⭕
# ------------------------------------------------------------------------------------
# 먼저 8x8로 잘랐다고 가정하면 두개의 체스판을 만들 수 있다. (top-left가 W인것/B인것)
# 두개를 비교해서 숫자가 작은 개수 출력하도록
    
base_W = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
base_B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

# Input값 받기
import sys
N, M = map(int, sys.stdin.readline().split())
chase = []
for i in range(N) : 
    row = list(sys.stdin.readline())
    chase.append(row)


# 8x8로 만들기
nn = []
for m in range(M-7) :
    for n in range(N-7) : 
        make_chase = []
        make_chase.append(chase[n][m:m+8])
        make_chase.append(chase[n+1][m:m+8])
        make_chase.append(chase[n+2][m:m+8])
        make_chase.append(chase[n+3][m:m+8])
        make_chase.append(chase[n+4][m:m+8])
        make_chase.append(chase[n+5][m:m+8])
        make_chase.append(chase[n+6][m:m+8])
        make_chase.append(chase[n+7][m:m+8])

        n_w = 0
        n_b = 0
        for i in range(8) :
            for j in range(8) :
                if make_chase[i][j] != base_W[i][j] :
                    n_w += 1
                if make_chase[i][j] != base_B[i][j] :
                    n_b += 1
        nn.append(n_w)
        nn.append(n_b)

print(min(nn))

