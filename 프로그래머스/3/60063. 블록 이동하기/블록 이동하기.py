def solution(board):
    from collections import deque
    def in_Range(lx, ly, rx, ry):
        return 0 <= lx < n and 0 <= ly < n and 0 <= rx < n and 0 <= ry < n

    def get_next_pos(cur_pos, board):
        next_pos = []
        pos = list(cur_pos)
        lx, ly, rx, ry = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
        # 상하좌우 확인
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nlx, nly, nrx, nry = lx+dx, ly+dy, rx+dx, ry+dy
            if in_Range(nlx, nly, nrx, nry):
                if board[nlx][nly] == 0 and board[nrx][nry] == 0:
                    next_pos.append(set([(nlx, nly), (nrx, nry)]))
        
        # 가로 방향 - 회전 확인
        if lx == rx:
            for i in [1, -1]:
                if in_Range(lx+i, ly, rx+i, ry):
                    if board[lx+i][ly] == 0 and board[rx+i][ry] == 0:
                        next_pos.append(set([(lx, ly), (lx+i, ly)]))
                        next_pos.append(set([(rx, ry), (rx+i, ry)]))

        # 세로 방향 - 회전 확인
        if ly == ry:
            for i in [1, -1]:
                if in_Range(lx, ly+i, rx, ry+i):
                    if board[lx][ly+i] == 0 and board[rx][ry+i]:
                        next_pos.append(set([(lx, ly), (lx, ly+i)]))
                        next_pos.append(set([(rx, ry), (rx, ry+i)]))
        return next_pos
    
    n = len(board)
    robot_pos = set([(0, 0), (0, 1)])
    q = deque()
    q.append((robot_pos, 0))
    visited = set()
    visited.add(frozenset(robot_pos))
    while q:
        cur_pos, cost = q.popleft()
        if (n-1, n-1) in cur_pos:
            return cost
        for next_pos in get_next_pos(cur_pos, board):
            if frozenset(next_pos) not in visited:
                q.append((next_pos, cost+1))
                visited.add(frozenset(next_pos))
    return -1