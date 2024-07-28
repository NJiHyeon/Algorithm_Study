import sys
from collections import deque 
from itertools import combinations 

# 입력 받기
input = sys.stdin.readline
N, M = map(int, input().split())
row_len = col_len = N
board = [list(map(int, input().split())) for _ in range(row_len)]

# 초기 설정
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# board 전처리
virus = []
for r in range(row_len):
    for c in range(col_len):
        if board[r][c] == 0:
            board[r][c] = '_'
        elif board[r][c] == 1:
            board[r][c] = '-'
        else:
            board[r][c] = '*'
            virus.append((r, c))

# bfs
def in_Range(r, c):
    return 0 <= r < row_len and 0 <= c < col_len

def bfs(v):
    # v : [[r, c], ..., [r, c]]
    new_board = [board[i][:] for i in range(row_len)]
    q = deque()
    result = 0
    for v_r, v_c in v:
        q.append((v_r, v_c, 0))
        new_board[v_r][v_c] = 0
    
    while q:
        cur_r, cur_c, cur_n = q.popleft() #1, 5, 0
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            next_n = cur_n + 1
            if in_Range(next_r, next_c) :
                if new_board[next_r][next_c] == '_':
                    q.append((next_r, next_c, next_n))
                    new_board[next_r][next_c] = next_n
                    result = max(next_n, result)
                elif new_board[next_r][next_c] == '*':
                    q.append((next_r, next_c, next_n))
                    new_board[next_r][next_c] = next_n

    for r in range(row_len):
        for c in range(col_len):
            if new_board[r][c] == '_':
                return -1 
    return result


# main
final_result = -1
for v in combinations(virus, M):
    result = bfs(v)
    if result != -1 and final_result != -1:
        final_result = min(result, final_result)
    elif result != -1 and final_result == -1:
        final_result = result

print(final_result)