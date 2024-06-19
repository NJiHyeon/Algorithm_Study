def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees :
        skill_index = []
        for k in s :
            if k in skill :
                skill_index.append(skill.index(k))
        if len(skill_index) != 0 :
            big = max(skill_index)
            if skill_index == [i for i in range(big+1)] :
                answer += 1
        else :
            answer += 1
    return answer