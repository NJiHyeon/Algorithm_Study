row_len, col_len = map(int, input().split())
board = [list(input().strip()) for _ in range(row_len)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for r in range(row_len):
    for c in range(col_len):
        if board[r][c] == 'R':
            red_r = r
            red_c = c
        elif board[r][c] == 'B':
            blue_r = r
            blue_c = c
        elif board[r][c] == 'O':
            target_r = r
            target_c = c 

def move(cur_r, cur_c, i):
    move_n = 0
    while board[cur_r+dr[i]][cur_c+dc[i]] != '#' and board[cur_r][cur_c] != 'O':
        cur_r += dr[i]
        cur_c += dc[i]
        move_n += 1
    return cur_r, cur_c, move_n
        
def dfs(red_r, red_c, blue_r, blue_c, cur_n):
    if cur_n >= 10:
        return 0
    for i in range(4):
        # 중력 이동
        next_red_r, next_red_c, move_red_n = move(red_r, red_c, i)
        next_blue_r, next_blue_c, move_blue_n = move(blue_r, blue_c, i)
        # 현재 위치를 기준으로 비교 
        if (next_red_r, next_red_c, next_blue_r, next_blue_c) in visit:
            continue
        if (next_blue_r, next_blue_c) == (target_r, target_c): #여기서 틀린점 : 파랑색이 구멍에 빠졌지만, 다른 방향은 괜찮을 수도 있으니까 return이 아니라 continue
            continue
        if (next_red_r, next_red_c) == (target_r, target_c):
            return 1
        if (next_red_r, next_red_c) == (next_blue_r, next_blue_c):
            if move_red_n > move_blue_n:
                next_red_r -= dr[i]
                next_red_c -= dc[i]
            else:
                next_blue_r -= dr[i]
                next_blue_c -= dc[i]
        # 재귀호출 (visit)
        visit.append((next_red_r, next_red_c, next_blue_r, next_blue_c))
        # 여기서 0이면 return 0을 안하는 이유는 하나의 깊이가 0이라고 전체 결과가 0인 것은 아니니까
        if dfs(next_red_r, next_red_c, next_blue_r, next_blue_c, cur_n+1) == 1:
            return 1
        visit.pop()
    return 0

visit = []
visit.append((red_r, red_c, blue_r, blue_c))
result = dfs(red_r, red_c, blue_r, blue_c, 0)
print(result)