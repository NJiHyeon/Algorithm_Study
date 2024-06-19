def solution(people, limit):
    answer = 0
    p=[]
    people.sort(reverse=True)
    for i in range(len(people)) :
        if len(p)==0 :
            p.append(people[i])
        else :
            if p[-1]+people[i] <= limit :
                answer += 1
                p.pop()
            else :
                p.append(people[i])
    return answer + len(p)
