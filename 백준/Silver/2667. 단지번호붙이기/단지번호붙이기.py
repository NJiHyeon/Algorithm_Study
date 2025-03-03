from collections import deque

# 1. 입력받기
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

row_len = len(graph)
col_len = len(graph[0])

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# 2. bfs
def bfs(r, c):
    n = 1
    q = deque()
    q.append((r, c))
    visit[r][c] = True

    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                if graph[next_r][next_c] == 1:
                    if visit[next_r][next_c] == False:
                        n += 1
                        q.append((next_r, next_c))
                        visit[next_r][next_c] = True
    return n


total_n = []
visit = [[False for _ in range(col_len)] for _ in range(row_len)]
for r in range(row_len):
    for c in range(col_len):
        if graph[r][c] == 1 and visit[r][c] == False:
            total_n.append(bfs(r, c))

total_n.sort()
print(len(total_n))
for tn in total_n:
    print(tn)