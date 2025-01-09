def solution(relation):
    col_name = 'abcdefgh'[:len(relation[0])]
    # 부분 집합
    def backtrack(curr, cur_i, k):
        # base case
        if len(curr) == k:
            combi.append(curr[:])  
        # repeat
        for j in range(cur_i, len(col_name)):
            curr.append(col_name[j])
            backtrack(curr, j+1, k)
            curr.pop()
    combi = []
    for k in range(1, len(col_name)+1):
        backtrack([], 0, k)

    # Table
    student_table = {}
    for r in range(len(relation)):
        for c in range(len(relation[0])):
            if col_name[c] not in student_table:
                student_table[col_name[c]] = [relation[r][c]]
            else:
                student_table[col_name[c]].append(relation[r][c])

    output = []
    # 유일성
    for cur_combi in combi: #['b', 'c']
        # 최소성
        ok = True
        for out in output:
            if set(out).issubset(set(cur_combi)):
                ok = False
                break
        if ok == False:
            continue
        students = []
        for r in range(len(relation)):
            student = ''
            for c in cur_combi:
                student += student_table[c][r]
            students.append(student)
        if len(relation) == len(set(students)): #유일성만족
            output.append(cur_combi)
            
    return len(output)           
            
            