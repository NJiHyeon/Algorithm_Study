from collections import deque 

def bfs(graph, start_v):
    q = deque()
    q.append(start_v)
    visit = []
    visit.append(start_v)
    while q:
        cur_v = q.popleft()
        for next_v in graph[cur_v]:
            if next_v not in visit:
                q.append(next_v)
                visit.append(next_v)
    return visit
            

def dfs(graph, start_v, visit):
    visit.append(start_v)
    for next_v in graph[start_v]:
        if next_v not in visit:
            dfs(graph, next_v, visit)
    return visit


# 입력 받기 
N, M, V = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for n in range(1, N+1):
    graph[n].sort()

# BFS, DFS 수행 
d_arr = dfs(graph, V, [])
for d in d_arr:
    print(d, end=" ")
print()
b_arr = bfs(graph, V)
for b in b_arr:
    print(b, end=" ")