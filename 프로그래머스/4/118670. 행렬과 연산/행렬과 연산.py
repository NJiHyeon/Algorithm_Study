def solution(rc, operations):
    from collections import deque
    row_len = len(rc)
    col_len = len(rc[0])
    
    # 새로운 행렬 형태 만들기
    start = deque()
    mid = deque()
    end = deque()
    for i in range(len(rc)):
        start.append(rc[i][0])
        mid.append(deque(rc[i][1:col_len-1]))
        end.append(rc[i][col_len-1])

    for op in operations:
        # 각 열끼리(start, mid, end) 행 순서에 따라 저장되어 있으므로 rotate를 실행하면 자동으로 행 변환
        if op == "ShiftRow":
            start.rotate()
            mid.rotate()
            end.rotate()
            
        # for문 필요 없이 열(start, mid, end)이 바뀌는 부분만 보면 된다. 
        elif op == "Rotate":
            # 1. start -> mid
            mid[0].appendleft(start.popleft())
            # 2. mid -> end
            end.appendleft(mid[0].pop())
            # 3. end -> mid
            mid[row_len-1].append(end.pop())
            # 4. mid -> start
            start.append(mid[row_len-1].popleft())
            
    result = []
    for i in range(len(rc)):
        result.append([start[i]] + list(mid[i]) + [end[i]])
    return result
        