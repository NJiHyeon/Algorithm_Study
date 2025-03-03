# 1. 입력받기
N = int(input())
a, b = map(int, input().split())
M = int(input())
graph = {i:[] for i in range(1, N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [False] * (N+1)
def dfs(cur_v, n):
    visit[cur_v] = True
    if cur_v == b:
        return n
    for next_v in graph[cur_v]:
        if visit[next_v] == False:
            result = dfs(next_v, n+1)
            if result != -1:
                return result

    visit[cur_v] = False
    return -1

print(dfs(a, 0))