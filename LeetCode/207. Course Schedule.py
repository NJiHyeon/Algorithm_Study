numCourses = 2
prerequisites = [[1,0]]
from collections import deque 

def topological_sort(numCourses, prerequisites):
    # 그래프(방향 주의), visited, indegree 설정
    graph = [[] for _ in range(numCourses)]
    visited = []
    indegree = [0] * numCourses

    # graph
    for v, u in prerequisites:
        graph[u].append(v)
        indegree[v] += 1

    # 위상정렬 수행
    q = deque()
    for v in range(numCourses):
        if indegree[v] == 0:
            q.append(v)

    while q:
        cur_v = q.popleft()
        visited.append(cur_v)
        for next_v in graph[cur_v]:
            indegree[next_v] -= 1
            if indegree[next_v] == 0:
                q.append(next_v)
    return visited

visited = topological_sort(numCourses, prerequisites)


