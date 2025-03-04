from collections import deque

# 1. 입력받기
M, N, H = map(int, input().split())
graph = []
target_tomato = 0

q = deque()
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

for h in range(H):
    h_graph = []
    for r in range(N):
        rc_graph = list(map(int, input().split()))
        for c in range(M):
            if rc_graph[c] == 0:
                target_tomato += 1
            elif rc_graph[c] == 1:
                q.append((h, r, c, 0))
                visited[h][r][c] = True
        h_graph.append(rc_graph)
    graph.append(h_graph)

# 2. bfs
def bfs(q):
    tomato_ripen_n = 0
    while q:
        cur_h, cur_r, cur_c, cur_n = q.popleft()
        for i in range(6):
            next_h = cur_h + dh[i]
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            next_n = cur_n + 1
            if 0 <= next_h < H and 0 <= next_r < N and 0 <= next_c < M:
                if graph[next_h][next_r][next_c] == 0:
                    if visited[next_h][next_r][next_c] == False:
                        q.append((next_h, next_r, next_c, next_n))
                        visited[next_h][next_r][next_c] = True
                        tomato_ripen_n += 1
                        if tomato_ripen_n == target_tomato:
                            return next_n
    return -1


# 전체과정
row_len = H
col_len = M
dh = [0, 0, 0, 0, 1, -1]
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]

if target_tomato == 0:
    print(0)
else:
    result = bfs(q)
    if result != -1:
        print(result)
    else:
        print(-1)