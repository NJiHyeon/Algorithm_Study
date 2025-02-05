def solution(queue1, queue2):
    from collections import deque 
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cur1 = sum(queue1)
    cur2 = sum(queue2)
    target = (cur1+cur2)//2
    result = 0
    l = 2*(len(queue1) + len(queue2)) 
    
    while result < l:
        if cur1 == cur2:
            return result 
        elif cur1 > cur2:
            c1 = queue1.popleft()
            queue2.append(c1)
            cur1 -= c1
            cur2 += c1
            result += 1
        else:
            c2 = queue2.popleft()
            queue1.append(c2)
            cur1 += c2
            cur2 -= c2
            result += 1
    if result == l:
        return -1
    return result