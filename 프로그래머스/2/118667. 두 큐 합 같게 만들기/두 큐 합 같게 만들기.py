def solution(queue1, queue2):
    from collections import deque
    m = 4*len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    l = sum(queue1)
    r = sum(queue2)
    answer = 0
    n = 0
    
    if (l+r) % 2 == 1 :
        return -1
    
    while queue1 and queue2 and n<m :
        n += 1
        if l > r :
            q1 = queue1.popleft()
            queue2.append(q1)
            answer += 1
            l -= q1
            r += q1
        elif l < r :
            q2 = queue2.popleft()
            queue1.append(q2)
            answer += 1
            l += q2
            r -= q2
        else :
            return answer
    return -1