from collections import deque 

def bfs(graph, r, c):
    q = deque()
    q.append((r, c, 1))
    visit = []
    visit.append((r, c))

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while q:
        cur_r, cur_c, cur_n = q.popleft()
        if cur_r == row_len-1 and cur_c == col_len-1:
            return cur_n
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                if graph[next_r][next_c] == '1':
                    if (next_r, next_c) not in visit:
                        q.append((next_r, next_c, cur_n+1))
                        visit.append((next_r, next_c))

N, M = map(int, input().split())
row_len = N
col_len = M
graph = []
for _ in range(N):
    graph.append(input().strip())
print(bfs(graph, 0, 0))