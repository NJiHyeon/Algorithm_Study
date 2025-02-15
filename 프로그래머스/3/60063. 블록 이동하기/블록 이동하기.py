def solution(board):
    from collections import deque 
    row_len = col_len = N = len(board)
    new_board = [[1 for _ in range(len(board))]]
    for b in board:
        new_board.append([1] + b)

    dar = [-1, 1, 0, 0]
    dac = [0, 0, -1, 1]
    dbr = [-1, 1, 0, 0]
    dbc = [0, 0, -1, 1]

    def make_visit(ar, ac, br, bc):
        return tuple(sorted([(ar, ac), (br, bc)]))
        
    def bfs(ar, ac, br, bc, n, d):
        q = deque()
        q.append([ar, ac, br, bc, n, d])
        visit = set()
        visit.add(make_visit(ar, ac, br, bc))
        d_dict = {'가로':'세로', '세로':'가로'}

        while q:
            ar, ac, br, bc, n, d = q.popleft()
            if ((ar, ac) == (N, N)) or ((br, bc) == (N, N)):
                return n
            
            for i in range(4):
                next_ar = ar + dar[i]
                next_ac = ac + dac[i]
                next_br = br + dbr[i]
                next_bc = bc + dbc[i]
                next_n = n + 1
                next_v = make_visit(next_ar, next_ac, next_br, next_bc)
                if 0 < next_ar <= row_len and 0 < next_ac <= col_len and 0 < next_br <= row_len and 0 < next_bc <= col_len:
                    if new_board[next_ar][next_ac] == 0 and new_board[next_br][next_bc] == 0:
                        if next_v not in visit:
                            q.append([next_ar, next_ac, next_br, next_bc, next_n, d])
                            visit.add(next_v)

                            if (i==0 and d=='가로') or (i==2 and d=='세로'):
                                rotation1 = make_visit(next_ar, next_ac, ar, ac)
                                if rotation1 not in visit:
                                    q.append([next_ar, next_ac, ar, ac, next_n, d_dict[d]])
                                    visit.add(rotation1)
                                rotation2 = make_visit(next_br, next_bc, br, bc)
                                if rotation2 not in visit:
                                    q.append([next_br, next_bc, br, bc, next_n, d_dict[d]])
                                    visit.add(rotation2)
                            elif (i==1 and d=='가로') or (i==3 and d=='세로'):
                                rotation1 = make_visit(ar, ac, next_ar, next_ac)
                                if rotation1 not in visit:
                                    q.append([ar, ac, next_ar, next_ac, next_n, d_dict[d]])
                                    visit.add(rotation1)
                                rotation2 = make_visit(br, bc, next_br, next_bc)
                                if rotation2 not in visit:
                                    q.append([br, bc, next_br, next_bc, next_n, d_dict[d]])
                                    visit.add(rotation2)

    result = bfs(1, 1, 1, 2, 0, '가로')
    return result