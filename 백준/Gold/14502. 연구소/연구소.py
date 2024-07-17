import sys
import copy
input = sys.stdin.readline
row_len, col_len = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row_len)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(new_graph, r, c):
    visited[r][c] = True 
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < row_len and 0 <= next_c < col_len and new_graph[next_r][next_c] == 0:
            if not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                new_graph[next_r][next_c] = 2
                dfs(new_graph, next_r, next_c)
    return new_graph

# 0 위치
location = []
for r in range(row_len):
    for c in range(col_len):
        if graph[r][c] == 0:
            location.append((r, c))
# 3개 뽑기 (조합)
answer = []
def backtracking(start_index, curr):
    if len(curr) == 3:
        answer.append(curr[:])
        return 
    for i in range(start_index, len(location)):
        curr.append(location[i])
        backtracking(i+1, curr)
        curr.pop()
    return answer
result = backtracking(0, [])

import copy
final = 0
for l in result:
    new_graph = copy.deepcopy(graph)
    # 벽 세우기
    new_graph[l[0][0]][l[0][1]] = 1
    new_graph[l[1][0]][l[1][1]] = 1
    new_graph[l[2][0]][l[2][1]] = 1

    # 새로 벽을 세운 그래프에 대해 탐색
    n_result = 0
    visited = [[False]*col_len for _ in range(row_len)]
    for r in range(row_len):
        for c in range(col_len):
            if new_graph[r][c] == 2 and visited[r][c] == False:
                new_graph = dfs(new_graph, r, c)
    for i in range(row_len):
        for j in range(col_len):
            if new_graph[i][j] == 0:
                n_result += 1
    if n_result > final:
        final = n_result
print(final)
