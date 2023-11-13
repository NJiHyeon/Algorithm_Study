import collections
def solution(k, tangerine):
    answer = 0 #서로 다른 종류의 수
    n = 0 #k와 비교할 수
    dict = collections.Counter(tangerine)
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    if dict[0][1] > k :
        return 1
    else :
        for i in range(len(dict)) :
            if n+dict[i][1] < k :
                n+=dict[i][1]
                answer+=1
            else :
                return answer+1

        
            
    