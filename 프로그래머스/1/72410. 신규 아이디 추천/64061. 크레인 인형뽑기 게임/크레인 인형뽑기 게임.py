def solution(board, moves):
    # [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    # [[], [0, 0,0,0,0,0],[0, 0,0,1,0,3],[0, 0,2,5,0,1],[0, 4,2,4,4,2],[0, 3,5,1,3,1]]
    r = 0
    doll = [101, 102]
    board.insert(0, [0]*len(board[0]))
    for bo in board : 
        bo.insert(0, [0])
        
    for m in moves :
        for i in range(1, len(board)) :
            if board[i][m] != 0 :
                doll.append(board[i][m])
                board[i][m] = 0
                if doll[-1] == doll[-2] :
                    doll.pop(-1)
                    doll.pop(-1)
                    r += 2
                break
    return r

    