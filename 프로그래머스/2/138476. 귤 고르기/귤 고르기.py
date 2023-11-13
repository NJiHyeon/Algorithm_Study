import collections
def solution(k, tangerine):
    answer = 0 #서로 다른 종류의 수
    n = 0 #k와 비교할 수
    dict = collections.Counter(tangerine)
    dict = sorted(dict.values(), reverse=True)
    if dict[0] > k :
        return 1
    else :
        for i in range(len(dict)) :
            if n+dict[i] < k :
                n+=dict[i]
                answer+=1
            else :
                return answer+1

        
            
    