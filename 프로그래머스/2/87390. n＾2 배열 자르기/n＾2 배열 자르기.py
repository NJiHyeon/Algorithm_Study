def solution(n, left, right) :
    answer = []
    for index in range(left, right+1) :
        i = index//n + 1
        j = index%n +1

        if n*n <=index :
            break
        if i>=j :
            answer.append(i)
        else :
            answer.append(j)
    return answer