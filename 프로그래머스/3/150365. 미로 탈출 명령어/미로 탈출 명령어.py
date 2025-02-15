def solution(n, m, x, y, r, c, k):
    from collections import deque
    board = [['.' for _ in range(m)] for _ in range(n)]
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    board[x][y] = 'S'
    board[r][c] = 'E'
    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]
    direct_dict = {0:'u', 1:'r', 2:'l', 3:'d'}
    
    stack = [(x, y, '', 0)]
    while stack:
        cur_r, cur_c, cur_str, cur_l = stack.pop()
        # base case
        if board[cur_r][cur_c] == 'E' and cur_l == k:
            return cur_str
        
        # repeat
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            next_str = cur_str + direct_dict[i]
            next_l = cur_l + 1
            if 0 <= next_r < n and 0 <= next_c < m:
                rest = k - next_l
                dist = abs(next_r-r) + abs(next_c-c)
                if rest >= dist and (rest-dist)%2 == 0:
                    stack.append([next_r, next_c, next_str, next_l])

    return 'impossible'