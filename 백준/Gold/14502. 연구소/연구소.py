import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
row_len, col_len = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row_len)]

def in_Range(r, c):
    return 0 <= r < row_len and 0 <= c < col_len

# bfs/dfs code
def bfs(graph):
    answer = 0
    new_graph = [graph[i][:] for i in range(row_len)]
    q = deque(virus)

    while q:
        cur_r, cur_c = q.popleft()
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if in_Range(next_r, next_c):
                if new_graph[next_r][next_c] == 0:
                    new_graph[next_r][next_c] = 2
                    q.append((next_r, next_c))

    # 0 개수 
    for r in range(row_len):
        for c in range(col_len):
            if new_graph[r][c] == 0:
                answer += 1
    return answer


# main code
    # 벽 3개 선택
    # dfs/bfs
    # max update
empty = []
virus = []
for r in range(row_len):
    for c in range(col_len):
        if graph[r][c] == 0:
            empty.append((r, c))
        elif graph[r][c] == 2:
            virus.append((r, c))

result = 0
for virus_cand in combinations(empty, 3):
    # 3개의 벽 선택
    # 벽을 새로 세운다.
    for i in range(3):
        graph[virus_cand[i][0]][virus_cand[i][1]] = 1
    # bfs 수행
    bfs_result = bfs(graph)
    if bfs_result > result:
        result = bfs_result
    # 세운 벽을 다시 되돌린다.
    for i in range(3):
        graph[virus_cand[i][0]][virus_cand[i][1]] = 0

print(result)
