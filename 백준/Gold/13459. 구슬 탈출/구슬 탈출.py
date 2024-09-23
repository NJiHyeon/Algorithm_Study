from sys import stdin as s

N, M = map(int, s.readline().split())
row_len = N
col_len = M
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
board = [s.readline().rstrip() for _ in range(N)]

for r in range(row_len):
    for c in range(col_len):
        if board[r][c] == 'R':
            red = (r, c)
        elif board[r][c] == 'B':
            blue = (r, c)
        elif board[r][c] == 'O':
            obj = (r, c)
visited = []
visited.append((red[0], red[1], blue[0], blue[1]))

def move(r, c, i):
    n = 0
    while board[r+dr[i]][c+dc[i]] != '#' and board[r][c] != "O":
        r += dr[i]
        c += dc[i]
        n += 1
    return r, c, n

def dfs(red, blue, move_n):
    if move_n > 10:
        return False
    
    for i in range(4):
        red_moved_r, red_moved_c, red_moved_n = move(red[0], red[1], i)
        blue_moved_r, blue_moved_c, blue_moved_n = move(blue[0], blue[1], i)
        if (red_moved_r, red_moved_c, blue_moved_r, blue_moved_c) in visited:
            continue
        if (blue_moved_r, blue_moved_c) == obj:
            continue
        if (red_moved_r, red_moved_c) == obj:
            return True
        if (red_moved_r, red_moved_c) == (blue_moved_r, blue_moved_c):
            if red_moved_n > blue_moved_n:
                red_moved_r -= dr[i]
                red_moved_c -= dc[i]
            else:
                blue_moved_r -= dr[i]
                blue_moved_c -= dc[i]
        visited.append((red_moved_r, red_moved_c, blue_moved_r, blue_moved_c))
        if dfs((red_moved_r, red_moved_c), (blue_moved_r, blue_moved_c), move_n + 1):
            return True
        visited.pop()
    return False
        

dfs_result = dfs(red, blue, 1)
if dfs_result == True:
    print(1)
else:
    print(0)