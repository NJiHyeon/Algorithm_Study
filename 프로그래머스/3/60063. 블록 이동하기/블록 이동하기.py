def solution(board):
    def in_Range(x, y):
        return 0 <= x < n and 0 <= y < n

    def get_next_pos(cur_pos, board):
        next_pos = []
        pos = list(cur_pos)
        lx, ly, rx, ry = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nlx, nly, nrx, nry = lx+dx, ly+dy, rx+dx, ry+dy
            if in_Range(nlx, nly) and in_Range(nrx, nry) and board[nlx][nly]==0 and board[nrx][nry] == 0:
                next_pos.append([(nlx, nly), (nrx, nry)])

        if lx == rx:
            for i in [1, -1]:
                if in_Range(lx+i, ly) and in_Range(rx+i, ry) and board[lx+i][ly] == 0 and board[rx+i][ry] == 0:
                    next_pos.append([(lx, ly), (lx+i, ly)])
                    next_pos.append([(rx, ry), (rx+i, ry)])

        if ly == ry:
            for i in [1, -1]:
                if in_Range(lx, ly+i) and in_Range(rx, ry+i) and board[lx][ly+i] == 0 and board[rx][ry+i] == 0:
                    next_pos.append([(lx, ly), (lx, ly+i)])
                    next_pos.append([(rx, ry), (rx, ry+i)])
        return next_pos
    
    from collections import deque
    n = len(board)
    # 로봇의 첫 위치
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