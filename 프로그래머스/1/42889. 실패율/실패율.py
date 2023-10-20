def solution(N, stages):
    fail = []
    l = len(stages)
    for i in range(1, N+1) : # 1단계부터 N단계까지 실패율
        if l == 0 :
            fail.append(0)
        else :
            a = stages.count(i)
            fail.append(a/l)
            l -= a
    index = sorted(range(len(fail)), key=lambda k: fail[k] , reverse=True) 
    answer = [i+1 for i in index]
    return answer