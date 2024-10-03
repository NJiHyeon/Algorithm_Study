from collections import deque 

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
row_len = col_len = N

# 1.각 요소 저장 및 보드 초기화
empty_n = 0
virus = []
wall = []
for r in range(row_len):
    for c in range(col_len):
        if board[r][c] == 0:
            empty_n += 1
            board[r][c] = '+'
        elif board[r][c] == 1:
            wall.append((r, c))
            board[r][c] = '-'
        else:
            virus.append((r, c))
            board[r][c] = '*'

# 2.바이러스 중에서 M개 조합 만들기
def backtracking(start, cur):
    # 탈출조건
    if len(cur) == M:
        combi.append(cur[:])
        return
    # 반복수행
    for i in range(start, len(virus)):
        if virus[i] not in cur:
            cur.append(virus[i])
            backtracking(i+1, cur)
            cur.pop()
combi = []
backtracking(0, [])

def bfs(board, cur_virus, entire_empty):
    new_board = [board[i][:] for i in range(row_len)]
    cur_empty = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    q = deque()
    visit = [[False for _ in range(col_len)] for _ in range(row_len)]
    for m in range(M):
        q.append((cur_virus[m][0], cur_virus[m][1], 0))
        visit[cur_virus[m][0]][cur_virus[m][1]] = True
    
    while q:
        if cur_empty == entire_empty:
            break
        cur_r, cur_c, cur_n = q.popleft()

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                if not visit[next_r][next_c]:
                    if new_board[next_r][next_c] == '+':
                        new_board[next_r][next_c] = cur_n + 1
                        q.append((next_r, next_c, cur_n+1))
                        visit[next_r][next_c] = True 
                        cur_empty += 1

                    elif new_board[next_r][next_c] == '*':
                        new_board[next_r][next_c] = cur_n + 1
                        q.append((next_r, next_c, cur_n+1))
                        visit[next_r][next_c] = True 

    for r in range(row_len):
        for c in range(col_len):
            if new_board[r][c] == '+':
                return 100000
    return q[-1][-1]


# 3.조합 돌면서
min_result = 100000
for cur_virus in combi:
    # 바이러스 활성화
    for m in range(M):
        board[cur_virus[m][0]][cur_virus[m][1]] = 0

    # BFS 실행
    result = bfs(board, cur_virus, empty_n)
    min_result = min(min_result, result)

    # 바이러스 비활성화
    for m in range(M):
        board[cur_virus[m][0]][cur_virus[m][1]] = '*'

if min_result == 100000:
    print(-1)
else:
    print(min_result)