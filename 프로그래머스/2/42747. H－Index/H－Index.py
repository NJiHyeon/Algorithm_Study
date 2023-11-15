def solution(citations):
    answer = []
    citations.sort() #	[10, 100]
    for i in range(len(citations)+1) :
        # 0번 이상 발표한 논문이 0편 이상 -> answer+1
        c_n = 0
        for c in citations :
            if i <= c :
                c_n += 1
        
        if i <= c_n :
            answer.append(i)
    return max(answer)