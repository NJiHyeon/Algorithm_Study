def solution(park, routes):
    '''
    park : ["SOO",
            "OOO",
            "OOO"]
    routes : ["E 2","S 2","W 1"]
    '''
    # h, w
    h = len(park)-1 #2
    w = len(park[0])-1 #2
    
    # set start index
    start = []
    for i in range(len(park)) :
        if "S" in park[i] :
            j = park[i].find("S")
            start.append(i)
            start.append(j) 
            
    # run routes : 공원을 벗어나는지 & 장애물 있는지 확인 잘하기
    for r in routes :
        if r[0] == "N" :
            # 장애물 확인하기 위해 가야할 step 만큼 O,X 문자열 만들기
            p = ''
            for s in range(1, int(r[2:])+1) :
                if start[0]-s >= 0 :
                    p += park[start[0]-s][start[1]]
                # 움직였을때 벗어나면 그만 만들기
                else :
                    break
            # 장애물 확인 및 공원을 벗어나는지 확인
            if (start[0]-int(r[2:]) >= 0) and ("X" not in p) :
                start[0] -= int(r[2:])
                
        elif r[0] == "S" : 
            p = ''
            for s in range(1, int(r[2:])+1) :
                if start[0]+s <= h :
                    p += park[start[0]+s][start[1]]
                else :
                    break
            if (start[0]+int(r[2:]) <= h) and ("X" not in p) :
                start[0] += int(r[2:])
                
        elif r[0] == "W" :
            p = ''
            for s in range(1, int(r[2:])+1) :
                if start[1]-s >= 0 :
                    p += park[start[0]][start[1]-s]
                else :
                    break
            if (start[1]-int(r[2:]) >= 0) and ("X" not in p) :
                start[1] -= int(r[2:])
                
        else : 
            p = ''
            for s in range(1, int(r[2:])+1) :
                if start[1]+s <= w :
                    p += park[start[0]][start[1]+s]
                else :
                    break
            if (start[1]+int(r[2:]) <= w) and ("X" not in p) :
                start[1] += int(r[2:])
            
    return start