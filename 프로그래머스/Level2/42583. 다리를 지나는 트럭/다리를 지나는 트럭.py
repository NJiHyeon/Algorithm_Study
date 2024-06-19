from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    bride_weight = 0
    
    while queue :
        answer += 1
        bw = queue.popleft()
        bride_weight -= bw
        
        if truck_weights :
            if bride_weight + truck_weights[0] <= weight :
                tw = truck_weights.popleft()
                queue.append(tw)
                bride_weight += tw
            else :
                queue.append(0)
    return answer