def solution(x, y, n):
    if x==y :
        return 0
    answer = 0
    queue = []
    queue.append([x]) #[[10]]

    while queue :
        start_list = queue.pop(0) #[10], queue:[]
        new = []
        answer += 1
        for i in range(len(start_list)) :
            if start_list[i]+n==y or start_list[i]*2==y or start_list[i]*3==y :
                return answer
            else :
                if start_list[i]+n<y :
                    new.append(start_list[i] + n)
                if start_list[i]*2<y :
                    new.append(start_list[i]*2)
                if start_list[i]*3<y :
                    new.append(start_list[i]*3)
        new = list(set(new))
        if new == [] :
            return -1
        else :
            queue.append(new)