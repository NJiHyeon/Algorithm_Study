from collections import deque

def solution(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])

    if grid[0][0] != 0 or grid[row-1][col-1] != 0 :
        return -1
    
    queue = deque()
    queue.append((0,0, 1)) #길이 정보까지 같이 주기!
    visited = [[False] * col for _ in range(row)]
    visited[0][0] = True

    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, 1, -1]

    while queue:
        cur_x, cur_y, cur_len  = queue.popleft()
        # 목적지에 도착했을 때, 그때의 cur_len을 shortest_path_len에 저장
        if cur_x == row-1 and cur_y == col-1 :
            shortest_path_len = cur_len
            # BFS는 완전탐색 임에도 불구하고 이 문제에서는 완전탐색이 필요 없으므로 break
            break

        for i in range(8):
            next_x = cur_x + dr[i]
            next_y = cur_y + dc[i]
            if 0<=next_x<col and 0<=next_y<row :
                if grid[next_x][next_y] == 0 and not visited[next_x][next_y] :
                    queue.append((next_x, next_y, cur_len+1))
                    visited[next_x][next_y] = True

    return shortest_path_len



print(solution(grid=[[0,0,0],[1,1,0],[1,1,0]]))
