def solution(n, s, a, b, fares):
    import heapq 
    graph = {i : [] for i in range(1, n+1)}
    for a_node, b_node, fare in fares:
        graph[a_node].append((b_node, fare))
        graph[b_node].append((a_node, fare))

    def dijkstra(graph, a, b, s, x, n):
        distances = [float("inf")] * (n+1)
        distances[x] = 0
        pq = [(0, x)]
        while pq:
            cur_cost, cur_v = heapq.heappop(pq)
            if distances[cur_v] < cur_cost:
                continue 
            for next_v, cost in graph[cur_v]:
                next_cost = distances[cur_v] + cost 
                if next_cost < distances[next_v]:
                    distances[next_v] = next_cost
                    heapq.heappush(pq, (next_cost, next_v))
        return distances[a]+distances[b]+distances[s]

    result = []
    for x in range(1, n+1):
        total_sum = dijkstra(graph, a, b, s, x, n)
        result.append(total_sum)
        
    return min(result)