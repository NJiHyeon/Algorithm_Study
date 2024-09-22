import sys
from sys import stdin as s
from collections import deque
from itertools import combinations

N, M = map(int, s.readline().split())
grid = [list(map(int, s.readline().split())) for _ in range(N)]
virus = []
entire_empty = 0
row_len = col_len = N
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for r in range(row_len):
    for c in range(col_len):
        if grid[r][c] == 0:
            grid[r][c] = '+'
            entire_empty += 1
        elif grid[r][c] == 1:
            grid[r][c] = '-'
        else:
            grid[r][c] = '*'
            virus.append((r, c))

def bfs(grid, virus_cand, empty):
    tmp = [grid[i][:] for i in range(row_len)]
    q = deque(virus_cand)
    while q:
        if empty == 0:
            return tmp[q[-1][0]][q[-1][1]]
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                if tmp[next_r][next_c] == '+':
                    empty -= 1
                    tmp[next_r][next_c] = tmp[cur_r][cur_c]+1
                    q.append((next_r, next_c))
                elif tmp[next_r][next_c] == '*':
                    tmp[next_r][next_c] = tmp[cur_r][cur_c]+1
                    q.append((next_r, next_c))
    return -1
    
result = 1000000
for virus_cand in combinations(virus, M):
    for vc in virus_cand:
        grid[vc[0]][vc[1]] = 0

    bfs_result = bfs(grid, virus_cand, entire_empty)
    if bfs_result != -1 and bfs_result < result:
        result = bfs_result

    for vc in virus_cand:
        grid[vc[0]][vc[1]] = '*'

if result == 1000000:
    print(-1)
else:
    print(result)