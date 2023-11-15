def solution(n, left, right) :
    answer = []
    for index in range(left+1, right+2) :
        i = index//n + 1
        j = index%n
        if j == 0 :
            i -= 1
            j = n
        if n*n <index :
            break
        if i>=j :
            answer.append(i)
        else :
            answer.append(j)
    return answer