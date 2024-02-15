def solution(rows, columns, queries):
    import copy
    answer = []
    # 1. init metrics 
    metric = [[((i-1)*columns + j) for j in range(1, columns+1)] for i in range(1, rows+1)]
    rotate_metric = [[((i-1)*columns + j) for j in range(1, columns+1)] for i in range(1, rows+1)]

    # 2. for문 돌면서 query 적용
    for q in queries: #q = [2,2,5,4]
        q_list = [] 
        m = metric[q[0]-1][q[1]-1]
        # rotate
        for i in range(q[0]-1, q[2]):
            if i == q[0]-1:
                rotate_metric[i][q[1]-1 : q[3]] = [metric[i+1][q[1]-1]] + metric[i][q[1]-1 : q[3]-1]
                if m > min(rotate_metric[i][q[1]-1 : q[3]]) :
                    m = min(rotate_metric[i][q[1]-1 : q[3]])
            elif i == q[2]-1:
                rotate_metric[i][q[1]-1 : q[3]] = metric[i][q[1] : q[3]] + [metric[i-1][q[3]-1]]
                if m > min(rotate_metric[i][q[1]-1 : q[3]]) :
                    m = min(rotate_metric[i][q[1]-1 : q[3]])
            else: 
                rotate_metric[i][q[1]-1] = metric[i+1][q[1]-1]
                rotate_metric[i][q[1] : q[3]-1] = metric[i][q[1] : q[3]-1]
                rotate_metric[i][q[3]-1] = metric[i-1][q[3]-1]
                if m > rotate_metric[i][q[1]-1] or m > rotate_metric[i][q[3]-1] :
                    m = min(rotate_metric[i][q[1]-1], rotate_metric[i][q[3]-1])
                
        #metric = copy.deepcopy(rotate_metric)
        metric = [item[:] for item in rotate_metric]
        answer.append(m)
    return answer