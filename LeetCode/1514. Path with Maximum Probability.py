import heapq

# Solution
#🧊 1. 그래프 먼저 만들기 (주의 방향 없는 그래프, 가중치 그래프)
graph = {}
n = 500
start_node = 4
end_node = 364
edges = [[193,229],[133,212],[224,465]]
succProb = [0.91,0.78,0.64]
for i, edge in enumerate(edges):
    # 우
    if edge[0] in graph:
        graph[edge[0]].append((edge[1], succProb[i]))
    else:
        graph[edge[0]] = [(edge[1], succProb[i])]
    # 좌
    if edge[1] in graph:
        graph[edge[1]].append((edge[0], succProb[i]))
    else:
        graph[edge[1]] = [(edge[0], succProb[i])]
graph

#🧊 2. 다익스트라로 최대 확률 계산
distances = [0.00001] * (n+1)
distances[start_node] = 1
pq = [(1, start_node)]

while pq:
    cur_dist, cur_v = heapq.heappop(pq)
    if distances[cur_v] > cur_dist:
        continue
    if cur_v not in graph:
        break
    for next_v, cost in graph[cur_v]:
        next_dist = distances[cur_v] * cost
        if next_dist > distances[next_v]:
            distances[next_v] = next_dist
            heapq.heappush(pq, (next_dist, next_v))