def solution(queue1, queue2):
    l = 0
    r = len(queue1)
    queue = queue1 + queue2
    left_sum = sum(queue[l:r])
    right_sum = sum(queue[r:])
    total_l = len(queue)
    result = 0
    while result < 2*total_l:
        if left_sum < right_sum:
            left_sum += queue[r]
            right_sum -= queue[r]
            r = (r+1)%total_l
            result += 1
        elif left_sum > right_sum:
            left_sum -= queue[l]
            right_sum += queue[l]
            l = (l+1)%total_l
            result += 1
        else:
            return result
    return -1