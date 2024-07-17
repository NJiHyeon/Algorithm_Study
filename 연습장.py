# 암시적 그래프 DFS
# 암시적으로 되어 있어서 우리가 찾아야하는, 조건을 잘 확인해야 하는 것들이 있다
    # 예를 들어, 범위를 넘는지 & 막혀있지 않은 v인지 확인하는 isValid
    # dfs를 쓸 때 for문에서 인접 리스트처럼 인접하는 노드가 바로 주어지지 않기 때문에 [cur_v]가 아니라 방향 개수에 따라 돌아야 한다.
    # 따라서 isValid 함수, dr, dc가 추가적으로 필요


    # 즉 일반적인 DFS와 다른점
        # 갈 수 있는 방향을 나타내는 dr, dc
        # 범위를 넘어가는지, 갈 수 있는 위치인지 확인하는 조건문
    # 같은점
        # 전체적인 구조
        # visited 표시해주기
def is_Valid(r, c):
    if 0 <= r < low_len and 0 <= c < col_len and grid[r][c] == 1:
        return True
def dfs(r, c):
    visited[r][c] = True
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if is_Valid(next_r, next_c):
            if not visited[next_r][next_c]:
                dfs(next_r, next_c)

grid = [...]
row_len = len(grid)
col_len = len(grid[0])
visited = [[False] * col_len for _ in range(row_len)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dfs(0, 0)

   


# 암시적 그래프 BFS




def dfs(r, c):
    visited[r][c] = True
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < row_len and 0 <= next_c < col_len and grid[next_r][next_c] == "1":
            if not visited[next_r][next_c]:
                dfs(next_r, next_c)


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
answer = 0
row_len, col_len = len(grid), len(grid[0])
visited = [[False]*col_len for _ in range(row_len)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for r in range(row_len):
    for c in range(col_len):
        if grid[r][c] == "1" and visited[r][c] == False:
            dfs(r, c)
            answer += 1

answer