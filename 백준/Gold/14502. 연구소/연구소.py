import sys
from collections import deque
from itertools import combinations

# 입력값 받기
input = sys.stdin.readline
row_len, col_len = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row_len)]

# 필요한 것 정의
wall_cand = []
virus_cand = []
for r in range(row_len):
    for c in range(col_len):
        if board[r][c] == 0:
            wall_cand.append((r, c))
        elif board[r][c] == 2:
            virus_cand.append((r, c))

def in_Range(r, c):
    return 0 <= r < row_len and 0 <= c < col_len 

# bfs
def bfs(board):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    new_board = [board[i][:] for i in range(row_len)]
    visited = [[False]*col_len for _ in range(row_len)]
    # 퍼뜨리기
    q = deque()
    for virus_r, virus_c in virus_cand:
        if not visited[virus_r][virus_c]:
            q.append((virus_r, virus_c))
            visited[virus_r][virus_c] = True 
            while q:
                cur_r, cur_c = q.popleft()
                for i in range(4):
                    next_r = cur_r + dr[i]
                    next_c = cur_c + dc[i]
                    if in_Range(next_r, next_c) and new_board[next_r][next_c] == 0:
                        if not visited[next_r][next_c]:
                            q.append((next_r, next_c))
                            visited[next_r][next_c] = True 
                            new_board[next_r][next_c] = 2
    
    
    # 안전영역 개수 세기
    safe_region = 0
    for r in range(row_len):
        for c in range(col_len):
            if new_board[r][c] == 0:
                safe_region += 1
    return safe_region




# main
result = 0
for wall in combinations(wall_cand, 3):
    # wall : [(r1, c1), (r2, c2), (r3, c3)]
    # 벽 세우기
    for wr, wc in wall:
        board[wr][wc] = 1

    # bfs로 바이러스 퍼뜨리기
    safe_region = bfs(board)
    result = max(result, safe_region)

    # 다시 벽 되돌리기
    for wr, wc in wall:
        board[wr][wc] = 0


print(result)