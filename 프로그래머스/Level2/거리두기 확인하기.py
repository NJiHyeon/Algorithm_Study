def solution(places):
    answer = []
    for p in places :
        if dfs(p) == True :
            answer.append(1)
        else:
            answer.append(0)
    return answer

def dfs(p) :
    ewsn = [[0,1], [0,-1], [1,0], [-1,0]]
    for i in range(5):
        for j in range(5):
            if p[i][j] == "P" :
                for ij in ewsn :
                    new_i = i + ij[0]
                    new_j = j + ij[1]
                    if (0 <= new_i <= 4) and (0 <= new_j <= 4) :
                        # 옆 칸이 P일 경우 -> return False
                        if p[new_i][new_j] == "P" :
                            return False
                        # 옆 칸이 O일 경우 -> 한번더 동서남북 확인
                        elif p[new_i][new_j] == "O" :
                            for mn in ewsn :
                                nnew_i = new_i + mn[0]
                                nnew_j = new_j + mn[1]
                                if (0 <= nnew_i <= 4) and (0 <= nnew_j <= 4) :
                                    if p[nnew_i][nnew_j] == "P" and (i,j)!=(nnew_i,nnew_j) :
                                        return False
                        # 옆 칸이 X일 경우 -> pass
    return True
