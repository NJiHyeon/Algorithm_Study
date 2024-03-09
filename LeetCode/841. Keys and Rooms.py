rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]

# BFS
from collections import deque
def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)
    visited[0] = True
    q = deque()
    q.append(0)
    while q:
        cur_node = q.popleft()
        for c in rooms[cur_node] :
            if visited[c] == False :
                visited[c] = True
                q.append(c)
    if sum(visited) == len(rooms) :
        return True
    else :
        return False


# DFS
def canVisitAllRooms(rooms):
    visited = []
    def dfs(cur_v) :
        visited.append(cur_v)
        for c in rooms[cur_v] :
            if c not in visited :
                 dfs(c)
    dfs(0)
    if len(visited) == len(rooms) :
        return True
    else:
        return False

canVisitAllRooms(rooms)
