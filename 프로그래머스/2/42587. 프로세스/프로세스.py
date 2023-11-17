def solution(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True :
        cut = queue.pop(0) #큐!
        if any(cut[1] < q[1] for q in queue) : #큰 값이 하나라도 있으면
            queue.append(cut) #다시 추가
        else :
            answer += 1
            if cut[0] == location : #이걸위해 인덱스와 같이 저장
                return answer
        