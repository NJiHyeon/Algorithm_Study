import sys
from itertools import combinations
from collections import deque 

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# graph를 초기화한다.
    # 0 빈칸 -> '_'
    # 1 벽 -> '-'
    # 2 바이러스 -> 비활성 상태 '*'
virus = []
for r in range(N):
    for c in range(N):
        if graph[r][c] == 0:
            graph[r][c] = '_'
        elif graph[r][c] == 1:
            graph[r][c] = '-'
        else:
            graph[r][c] = '*'
            virus.append([r, c])

# bfs 
# 큐 생성하고, M개의 위치와 시간0을 입력
# 큐 반복
    # 상하좌우 시간 + 1씩
# 다 끝났을 때 이중 for문 돌면서 '_'(빈칸)이 있으면 -1 리턴하고 없으면 최댓값 리턴
def in_Range(r, c):
    return 0 <= r < N and 0 <= c < N

def bfs(v):
    level = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    q = deque()
    for v_r, v_c in v:  
        q.append([v_r, v_c, 0])
    new_graph = [graph[i][:] for i in range(N)]
    while q:
        cur_r, cur_c, cur_l = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            next_l = cur_l + 1
            if in_Range(next_r, next_c):
                if new_graph[next_r][next_c] == '_':
                    new_graph[next_r][next_c] = next_l
                    level = max(level, next_l)
                    q.append([next_r, next_c, next_l])
                elif new_graph[next_r][next_c] == '*':
                    new_graph[next_r][next_c] = next_l 
                    q.append([next_r, next_c, next_l])

    for r in range(N):
        for c in range(N):
            if new_graph[r][c] == '_':
                return -1
    return level

# main
# 바이러스의 위치를 담는다.
# 바이러스의 위치들 중 조합을 통해 M개 선택한다.
# M개 선택된 바이러스를 활성 상태로 바꾼다.
# bfs()
# 다시 비활성 상태로 바꾼다. 
final_level = -1
for v in combinations(virus, M):
    for v_r, v_c in v:
        graph[v_r][v_c] = 0
    level = bfs(v)
    if final_level == -1 and level != -1:
        final_level = level
    elif final_level != -1 and level != -1:
        final_level = min(final_level, level)
    for v_r, v_c in v:
        graph[v_r][v_c] = '*'
print(final_level)