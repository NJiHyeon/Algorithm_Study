from collections import deque

row_len, col_len = map(int, input().split())
board = []
for _ in range(row_len):
    board.append(input().strip())

for r in range(row_len):
    for c in range(col_len):
        if board[r][c] == 'B':
            b_r, b_c = r, c
        elif board[r][c] == 'R':
            r_r, r_c = r, c
        elif board[r][c] == 'O':
            o_r, o_c = r, c

def move(r, c, dr, dc):
    n = 0
    while board[r+dr][c+dc] != '#' and board[r][c] != 'O':
        r += dr 
        c += dc 
        n += 1
    return r, c, n

def bfs(rr, rc, br, bc):
    q = deque()
    visit = []
    q.append([rr, rc, br, bc, 0])
    visit.append([rr, rc, br, bc])
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while q:
        curr = q.popleft()
        cur_rr, cur_rc, cur_br, cur_bc, cur_n = curr[0], curr[1], curr[2], curr[3], curr[4]
        for i in range(4):
            next_rr, next_rc, rn = move(cur_rr, cur_rc, dr[i], dc[i])
            next_br, next_bc, bn = move(cur_br, cur_bc, dr[i], dc[i])
            next_n = cur_n + 1

            # 구슬확인
            if next_br == o_r and next_bc == o_c:
                continue
            elif next_rr == o_r and next_rc == o_c:
                return 1
            elif next_rr == next_br and next_rc == next_bc:
                if rn > bn:
                    next_rr -= dr[i]
                    next_rc -= dc[i]
                else:
                    next_br -= dr[i]
                    next_bc -= dc[i]

            if [next_rr, next_rc, next_br, next_bc] not in visit:
                if next_n < 10:
                    q.append([next_rr, next_rc, next_br, next_bc, next_n])
                    visit.append([next_rr, next_rc, next_br, next_bc])
    return 0


print(bfs(r_r, r_c, b_r, b_c))