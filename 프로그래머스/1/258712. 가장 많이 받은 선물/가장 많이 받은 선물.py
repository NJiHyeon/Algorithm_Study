def solution(friends, gifts):
    answer = 0
    stage1, stage2 = stage(friends, gifts)
    # i:준사람, j:받은사람
    for i in range(len(friends)) :
        i_answer = 0
        for j in range(len(friends)) :
            if i!=j and stage1[i][j] > stage1[j][i] :
                i_answer += 1
            elif i!=j and stage1[i][j] == stage1[j][i] and stage2[friends[i]]>stage2[friends[j]] :
                i_answer += 1
        if i_answer > answer :
            answer = i_answer
    return answer


def stage(friends, gifts) :
    stage1 = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    stage2 = {name: 0 for name in friends}
    for g in gifts:
        g_list = g.split(' ')
        p = g_list[0]
        m = g_list[1]
        p_i = friends.index(p)
        m_i = friends.index(m)
        stage1[p_i][m_i] += 1
        stage2[p] += 1
        stage2[m] -=1
    return stage1, stage2