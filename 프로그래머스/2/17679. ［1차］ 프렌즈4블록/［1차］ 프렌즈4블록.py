def solution(m, n, board):
    answer = 0
    for i in range(m) :
        board[i] = list(board[i])
    while True :
        b = 0
        kakao = {}
        # b개수 세기
        for i in range(m-1) :
            for j in range(n-1) :
                if board[i][j]!=' ' and board[i][j]==board[i][j+1] and board[i][j]==board[i+1][j] and board[i][j]==board[i+1][j+1] :
                    if board[i][j] not in kakao :
                        kakao[board[i][j]] = []
                        kakao[board[i][j]].append((i,j))
                        kakao[board[i][j]].append((i,j+1))
                        kakao[board[i][j]].append((i+1,j))
                        kakao[board[i][j]].append((i+1,j+1))
                        kakao[board[i][j]] = list(set(kakao[board[i][j]]))
                    else :
                        kakao[board[i][j]].append((i,j))
                        kakao[board[i][j]].append((i,j+1))
                        kakao[board[i][j]].append((i+1,j))
                        kakao[board[i][j]].append((i+1,j+1))
                        kakao[board[i][j]] = list(set(kakao[board[i][j]]))
        l = list(kakao.keys())
        if len(l)==0 :
            # 없으면 나오기
            break
        else :
            # 있으면 개수 세고 + 블록 내리기
            for icon in l :
                answer += len(kakao[icon])
                for matrix in kakao[icon] :
                    board[matrix[0]][matrix[1]] = ' '
                
            for i in range(n-1, -1, -1) : #세로줄 개수
                for j in range(m-1, -1, -1) : #가로줄 개수
                    if board[j][i] == ' ' :
                        for k in range(j-1, -1, -1) :
                            if board[k][i] != ' ' :
                                board[j][i]=board[k][i]
                                board[k][i] = ' '
                                break
    return answer