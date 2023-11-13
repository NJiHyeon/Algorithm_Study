def solution(k, tangerine):
    answer = 0
    n = 0
    import collections
    dict = collections.Counter(tangerine)
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    # [(3, 2), (2, 2), (5, 2), (1, 1), (4, 1)], k=6
    if dict[0][1] > k :
        return 1
    else :
        for i in range(len(dict)) :
            if n+dict[i][1] < k :
                n+=dict[i][1]
                answer+=1
            elif n+dict[i][1] == k :
                answer+=1
                return answer
            else :
                return answer+1
        
            
    