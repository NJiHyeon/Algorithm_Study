from collections import deque 

N, M = map(int, input().split())
row_len = N
col_len = M
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
graph = []

for _ in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

# 1. 녹이는 함수
def melt(graph):
    new_graph = [graph[i][:] for i in range(row_len)]

    for r in range(row_len):
        for c in range(col_len):
            if graph[r][c] > 0:
                adjacent_n = 0
                for i in range(4):
                    next_r = r + dr[i]
                    next_c = c + dc[i]
                    if 0 <= next_r < row_len and 0 <= next_c < col_len:
                        if graph[next_r][next_c] == 0:
                            adjacent_n += 1
                new_graph[r][c] = max(0, graph[r][c]-adjacent_n)
    return new_graph

# 2. 덩어리 새는 함수
def lump(r, c):
    q = deque()
    q.append((r, c))
    visit[r][c] = True 

    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                if graph[next_r][next_c] > 0:
                    if visit[next_r][next_c] == False:
                        q.append((next_r, next_c))
                        visit[next_r][next_c] = True
    return


# 3. 
year_n = 0
result = 0
while True:
    graph = melt(graph)
    year_n += 1 #출력
    lump_n = 0 #덩어리개수
    zero_n = 0 #0인 칸 개수
    visit = [[False for _ in range(col_len)] for _ in range(row_len)]
    for r in range(row_len):
        for c in range(col_len):
            if graph[r][c] > 0 and visit[r][c] == False:
                lump(r, c)
                lump_n += 1
            elif graph[r][c] == 0:
                zero_n += 1

    if lump_n >= 2:
        result = year_n
        break
    elif zero_n == row_len*col_len:
        result = 0
        break
print(result)