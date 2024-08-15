def solution(n, paths, gates, summits):
    import heapq
    summits.sort()
    
    graph = {}
    for path in paths:
        a, b, c = path[0], path[1], path[2]
        if a not in graph:
            graph[a] = [(b, c)]
        else:
            graph[a].append((b, c))
        if b not in graph:
            graph[b] = [(a, c)]
        else:
            graph[b].append((a, c))
    distances = [10000000] * (n+1)

    pq = []
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        distances[gate] = 0
    
    while pq:
        cur_dist, cur_v = heapq.heappop(pq)
        if distances[cur_v] < cur_dist or cur_v in summits:
            continue
        for next_v, cost in graph[cur_v]:
            next_dist = max(distances[cur_v], cost)
            if next_dist < distances[next_v]:
                distances[next_v] = next_dist
                heapq.heappush(pq, (next_dist, next_v))
    
    min_distance = [0, 10000001]
    for s in summits:
        if distances[s] < min_distance[1]:
            min_distance = [s, distances[s]]
    return min_distance