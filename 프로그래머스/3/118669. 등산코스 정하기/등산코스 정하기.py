def solution(n, paths, gates, summits):
    import heapq
    graph = {}
    for path in paths:
        if path[0] not in graph:
            graph[path[0]] = [(path[1], path[2])]
        else:
            graph[path[0]].append((path[1], path[2]))
        
        if path[1] not in graph:
            graph[path[1]] = [(path[0], path[2])]
        else:
            graph[path[1]].append((path[0], path[2]))

    pq = []
    min_result = [float("inf"), float("inf")]
    distances = [float("inf")] * (n+1)

    for gate in gates:
        heapq.heappush(pq, (0, gate))
        distances[gate] = 0

    while pq:
        cur_dist, cur_v = heapq.heappop(pq)
        if cur_dist > min_result[1]:
            break
        if cur_v in summits:
            if cur_dist < min_result[1]:
                min_result = [cur_v, cur_dist]
            if cur_v < min_result[0]:
                min_result[0] = cur_v
            continue

        for next_v, cost in graph[cur_v]:
            next_cost = max(distances[cur_v], cost)
            if next_cost < distances[next_v]:
                distances[next_v] = next_cost
                heapq.heappush(pq, (next_cost, next_v))
    return min_result