times = [[2,1,1],[2,3,1],[3,4,1]]
n = 2
k = 2

# 인접 리스트 형태로 만들기
# [start, end, cost]
graph = {}
for i in range(len(times)):
    if times[i][0] in graph:
        graph[times[i][0]].append((times[i][1], times[i][2]))
    else:
        graph[times[i][0]] = [(times[i][1], times[i][2])]
graph
# 다익스트라 템플릿
import heapq
distances = [float('INF')] * (n+1)
distances[k] = 0
pq = [(0, k)]

while pq:
    cur_dist, cur_v = heapq.heappop(pq)
    if cur_v not in graph:
        continue 
    if distances[cur_v] < cur_dist:
        continue
    for next_v, cost in graph[cur_v]:
        next_cost = distances[cur_v] + cost
        if next_cost < distances[next_v]:
            distances[next_v] = next_cost
            heapq.heappush(pq, (next_cost, next_v))
    
distances