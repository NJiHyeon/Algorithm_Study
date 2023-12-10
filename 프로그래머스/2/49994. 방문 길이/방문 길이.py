def solution(dirs):
    answer = 0
    current = (0,0)
    step = {"U":(0,-1), "D":(0,1), "R":(1,0), "L":(-1,0)}
    rec = []
    for d in dirs :
        new_x = current[0] + step[d][0]
        new_y = current[1] + step[d][1]
        if new_x < -5 or new_x >5 or new_y < -5 or new_y > 5 :
            continue
        if ((current[0], current[1], new_x, new_y) not in rec) and ((new_x, new_y, current[0], current[1]) not in rec) :
            answer += 1
            rec.append((current[0], current[1], new_x, new_y))
            rec.append((new_x, new_y, current[0], current[1]))
        current = (new_x, new_y)
        
    return answer