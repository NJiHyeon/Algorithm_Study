from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    queue_sum = 0
    
    while queue :
        answer += 1
        queue_sum -= queue.popleft() #앞으로 한칸&다리무게
        # 추가 가능하면 트럭 추가, 아니면 0 추가
        if truck_weights :
            if queue_sum + truck_weights[0] <= weight :
                t = truck_weights.popleft()
                queue.append(t)
                queue_sum += t
            else :
                queue.append(0)
    return answer