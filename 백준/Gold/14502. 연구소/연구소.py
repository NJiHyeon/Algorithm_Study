from collections import deque 
import sys
from itertools import combinations

input = sys.stdin.readline
row_len, col_len = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(row_len)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
wall = []
wall_3 = []
virus = []

for r in range(row_len):
    for c in range(col_len):
        if grid[r][c] == 0:
            wall.append((r, c))
        elif grid[r][c] == 2:
            virus.append((r, c))

def combi(curr, curr_i):
    # 탈출 조건
    if len(curr) == 3:
        wall_3.append(curr[:])
        return
    # 반복 수행
    for i in range(curr_i, len(wall)):
        curr.append(wall[i])
        combi(curr, curr_i+1)
        curr.pop()


def bfs(grid, r, c):
    q = deque(virus)
    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                    if grid[next_r][next_c] == 0:
                        grid[next_r][next_c] = 2
                        q.append((next_r, next_c))

    l = 0
    for r in range(row_len):
        for c in range(col_len):
            if grid[r][c] == 0:
                l += 1
    return l

# 벽 세우기
max_safe = 0
for cur_wall in combinations(wall, 3):
    grid[cur_wall[0][0]][cur_wall[0][1]] = 1
    grid[cur_wall[1][0]][cur_wall[1][1]] = 1
    grid[cur_wall[2][0]][cur_wall[2][1]] = 1

    # 바이러스 퍼트리기
    copy_grid = [grid[i][:] for i in range(row_len)]
    bfs_result = bfs(copy_grid, r, c)

    # 안전영역 개수 세기
    max_safe = max(bfs_result, max_safe)

    # 되돌리기
    grid[cur_wall[0][0]][cur_wall[0][1]] = 0
    grid[cur_wall[1][0]][cur_wall[1][1]] = 0
    grid[cur_wall[2][0]][cur_wall[2][1]] = 0

print(max_safe)
