def solution(sequence, k):
    answer = []
    sum = 0
    l = 0
    r = 0
    while True :
        if sum < k :
            if r >= len(sequence) :
                break
            sum += sequence[r]
            r += 1
        else :
            if l >= len(sequence) :
                break
            sum -= sequence[l]
            l += 1
        if sum == k :
            answer.append([l,r-1])
    answer.sort(key=lambda x:(x[1]-x[0], x[0]))
    return answer[0]