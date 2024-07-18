import sys
from collections import deque

input = sys.stdin.readline
row_len, col_len = map(int, input().split())
board = [input().rstrip() for _ in range(row_len)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 최대한 움직일 수 있는 위치
def move(r, c, dr, dc):
    count = 0
    while board[r+dr][c+dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc 
        count += 1
    return r, c, count

# 빨강, 파랑 구슬 위치 찾기
for r in range(row_len):
    for c in range(col_len):
        if board[r][c] == 'R':
            rr, rc = r, c
        elif board[r][c] == 'B':
            br, bc = r, c

answer = 0
visited = set()
queue = deque()
queue.append([rr, rc, br, bc, 0])
visited.add((rr, rc, br, br))


while queue:
    cur_rr, cur_rc, cur_br, cur_bc, level = queue.popleft()
    if level >= 10:
        break 
    for i in range(4):
        # 방향은 한 방향인데, 한 칸만 움직일 수 있는게 아니다. 
        next_rr, next_rc, r_count = move(cur_rr, cur_rc, dr[i], dc[i])
        next_br, next_bc, b_count = move(cur_br, cur_bc, dr[i], dc[i])

        # 방문 했던 곳인지
        if (next_rr, next_rc, next_br, next_bc) in visited:
            continue

        # 파랑이 구멍에 빠졌는지
        if board[next_br][next_bc] == 'O':
            continue

        # 빨강이 구멍에 빠졌는지
        if board[next_rr][next_rc] == 'O':
            answer = 1
            break

        # 둘 다 안빠지고, 두개의 위치가 동일한지
        if next_rr == next_br and next_rc == next_bc:
            if r_count > b_count:
                next_rr -= dr[i]
                next_rc -= dc[i]
            else:
                next_br -= dr[i]
                next_bc -= dc[i]
        
        # 추가 및 방문
        queue.append([next_rr, next_rc, next_br, next_bc, level+1])
        visited.add((next_rr, next_rc, next_br, next_bc))

print(answer)