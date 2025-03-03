# 안전영역 : 물에 잠기지 않는 지점들이 (특정 값 초과) 상하좌우로 인접해 있으며 그 크기가 최대인 영역 
# 최대 개수  

from collections import deque
#1. 입력 받기
N = int(input())
graph = []
max_rain = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    max_rain = max(max_rain, max(temp))
    graph.append(temp)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

#2. bfs
def bfs(r, c, rain):
    q = deque()
    q.append((r, c))
    visit[r][c] = True 
    
    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                if visit[next_r][next_c] == False:
                    if graph[next_r][next_c] > rain:
                        q.append((next_r, next_c))
                        visit[next_r][next_c] = True
    return 

row_len = col_len = N
max_region = 0
for rain in range(0, max_rain+1):
    visit = [[False for _ in range(col_len)] for _ in range(row_len)]
    region = 0
    for r in range(row_len):
        for c in range(col_len):
            if graph[r][c] > rain and visit[r][c] == False:
                bfs(r, c, rain)
                region += 1
    max_region = max(max_region, region)
print(max_region)