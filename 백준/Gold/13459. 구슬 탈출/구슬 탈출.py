import sys 
from collections import deque 

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
# board = [list(map(int, input().split())) for _ in range(N)]

# 구슬 이동 함수
def move(r, c, dr, dc):
    count = 0
    while board[r+dr][c+dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc
        count += 1
    return r, c, count

# main
# R 위치 : 
# B 위치 : 
# 큐 생성
# 큐 append : [[r_r, r_c, 0], [b_r, b_c, 0]]
# visit : set() + Frize?
# while q
    # pop
    # for
        # next
        # move()
        # 조건 달기 
            # 만약 파랑이 구멍에 빠졌다면 continue
            # 만약 빨강이 구멍에 빠졌다면 return 1
            # 만약 둘 다 안빠지고 같은 곳에 있으면 더 많이 움직인 구슬 한칸 뒤로 이동 & append
blue = []
red = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 'B':
            blue.append(r)
            blue.append(c)
        elif board[r][c] == 'R':
            red.append(r)
            red.append(c)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer = 0
q = deque()
q.append([red[0], red[1], blue[0], blue[1], 0])
visited = set()
visited.add((red[0], red[1], blue[0], blue[1]))

while q:
    cur_rr, cur_rc, cur_br, cur_bc, cur_n = q.popleft()
    if cur_n >= 10:
        break
    for i in range(4):
        # 안헷갈리게 색깔별로 따로 이동함수 생성 
        next_rr, next_rc, next_rn = move(cur_rr, cur_rc, dr[i], dc[i])
        next_br, next_bc, next_bn = move(cur_br, cur_bc, dr[i], dc[i])
        # 그리고 나서 각 위치에 따른 조건 확인
        if (next_rr, next_rc, next_br, next_bc) in visited:
            continue 

        if board[next_br][next_bc] == 'O':
            continue 

        if board[next_rr][next_rc] == 'O':
            answer = 1
            break 

        if next_rr == next_br and next_rc == next_bc:
            if next_rn > next_bn:
                next_rr -= dr[i]
                next_rc -= dc[i]
            else:
                next_br -= dr[i]
                next_bc -= dc[i]
        q.append([next_rr, next_rc, next_br, next_bc, cur_n+1])
        visited.add((next_rr, next_rc, next_br, next_bc))

print(answer)