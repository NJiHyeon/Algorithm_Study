def solution(wallpaper):
    wall = []
    answer = []
    for i in range(len(wallpaper)) :
        for j in range(len(wallpaper[i])) :
            if wallpaper[i][j] == '#' :
                w = []
                w.append(i)
                w.append(j)
                wall.append(w)
    
    x = []
    y = []
    for w in wall :
        x.append(w[0])
        y.append(w[1])
    
    answer.append(min(x))
    answer.append(min(y))
    answer.append(max(x)+1)
    answer.append(max(y)+1)
    return answer