def solution(queue1, queue2):
    left = sum(queue1)
    right = sum(queue2)    
    queue = queue1 + queue2
    L = len(queue)
    cur_l = 0
    l = 0
    r = len(queue1)
    while cur_l < 2*L:
        if left == right:
            return cur_l
        elif left < right:
            left += queue[r]
            right -= queue[r]
            r += 1
            r %= L
            cur_l += 1
        elif left > right:
            left -= queue[l]
            right += queue[l]
            l += 1
            l %= L
            cur_l += 1
    return -1