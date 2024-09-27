def solution(n, s, a, b, fares):
    import heapq 
    graph = {}
    for fare in fares:
        if fare[0] not in graph:
            graph[fare[0]] = [(fare[1], fare[2])]
        else:
            graph[fare[0]].append((fare[1], fare[2]))
        if fare[1] not in graph:
            graph[fare[1]] = [(fare[0], fare[2])]
        else:
            graph[fare[1]].append((fare[0], fare[2]))

    taxi = []
    for start_v in [s, a, b]:
        distances = [float("inf")]*(n+1)
        distances[start_v] = 0
        pq = [(start_v, 0)]
        while pq:
            cur_v, cur_cost = heapq.heappop(pq)
            if distances[cur_v] < cur_cost:
                continue
            for next_v, cost in graph[cur_v]:
                next_cost = distances[cur_v] + cost 
                if next_cost < distances[next_v]:
                    distances[next_v] = next_cost
                    heapq.heappush(pq, (next_v, next_cost))
        taxi.append(distances[1:])
    
    result = float("inf")
    for i in range(n):
        if result > (taxi[0][i] + taxi[1][i] + taxi[2][i]):
            result = taxi[0][i] + taxi[1][i] + taxi[2][i]
    return result

