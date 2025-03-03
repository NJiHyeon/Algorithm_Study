from collections import deque 

# 1. 입력받기
N = int(input())
P = int(input())
graph = {i : [] for i in range(1, N+1)}
for _ in range(P):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 2. bfs
def bfs(graph, start_v):
    computer_n = 0
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
                computer_n += 1

    return computer_n

print(bfs(graph, 1))