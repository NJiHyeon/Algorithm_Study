def solution(board):
    from collections import deque 
    
    # 초기 설정
    row_len, col_len = len(board), len(board[0])
    def in_Range(r, c):
        return 0 <= r < row_len and 0 <= c < col_len and board[r][c] == 0
    
    # main = bfs 
    q = deque()
    q.append([(0, 0), (0, 1), 0])
    visited = set()
    visited.add(frozenset(((0, 0), (0, 1))))
    while q:
        cur1, cur2, cur_n = q.popleft()
        cur_r1, cur_c1 = cur1[0], cur1[1]
        cur_r2, cur_c2 = cur2[0], cur2[1]
        if (cur_r1, cur_c1) == (row_len-1, col_len-1) or (cur_r2, cur_c2) == (row_len-1, col_len-1):
            return cur_n
        
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  
            next_r1 = cur_r1 + dr
            next_c1 = cur_c1 + dc
            next_r2 = cur_r2 + dr
            next_c2 = cur_c2 + dc
            next_n = cur_n + 1
            if in_Range(next_r1, next_c1) and in_Range(next_r2, next_c2):
                if frozenset(((next_r1, next_c1), (next_r2, next_c2))) not in visited:
                    q.append([(next_r1, next_c1), (next_r2, next_c2), next_n])
                    visited.add(frozenset(((next_r1, next_c1), (next_r2, next_c2))))
        
        # 가로 방향
        if cur_r1 == cur_r2 :
            for dr, dc in [[1, 0], [-1, 0]]:
                next_r1 = cur_r1 + dr
                next_c1 = cur_c1 + dc
                next_r2 = cur_r2 + dr
                next_c2 = cur_c2 + dc
                next_n = cur_n + 1
                if in_Range(next_r1, next_c1) and in_Range(next_r2, next_c2):
                    if frozenset(((cur_r1, cur_c1), (next_r1, next_c1))) not in visited:
                        q.append([(cur_r1, cur_c1), (next_r1, next_c1), next_n])
                        visited.add(frozenset(((cur_r1, cur_c1), (next_r1, next_c1))))
                    if frozenset(((cur_r2, cur_c2), (next_r2, next_c2))) not in visited:
                        q.append([(cur_r2, cur_c2), (next_r2, next_c2), next_n])
                        visited.add(frozenset(((cur_r2, cur_c2), (next_r2, next_c2))))
        
        # 세로 방향
        if cur_c1 == cur_c2 :
            for dr, dc in [[0, 1], [0, -1]]:
                next_r1 = cur_r1 + dr
                next_c1 = cur_c1 + dc
                next_r2 = cur_r2 + dr
                next_c2 = cur_c2 + dc
                next_n = cur_n + 1
                if in_Range(next_r1, next_c1) and in_Range(next_r2, next_c2):
                    if frozenset(((cur_r1, cur_c1), (next_r1, next_c1))) not in visited:
                        q.append([(cur_r1, cur_c1), (next_r1, next_c1), next_n])
                        visited.add(frozenset(((cur_r1, cur_c1), (next_r1, next_c1))))
                    if frozenset(((cur_r2, cur_c2), (next_r2, next_c2))) not in visited:
                        q.append([(cur_r2, cur_c2), (next_r2, next_c2), next_n])
                        visited.add(frozenset(((cur_r2, cur_c2), (next_r2, next_c2))))
    
    
