def solution(clothes):
    dic = {}
    for cl in clothes :
        if cl[1] not in dic :
            dic[cl[1]] = 1
        else :
            dic[cl[1]] += 1
            
    answer = 1
    catego = list(dic.keys())
    for c in catego :
        answer *= (dic[c]+1)

    return answer-1