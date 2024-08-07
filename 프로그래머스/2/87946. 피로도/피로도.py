def solution(k, dungeons):
    n_list = []
    
    import itertools
    nPr = itertools.permutations(dungeons, len(dungeons))
    for d in nPr :
        kd = k
        n = 0
        for j in range(len(d)) :
            if kd >= d[j][0] :
                kd -= d[j][1]
                n += 1
        n_list.append(n)
    return max(n_list)