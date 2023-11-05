def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()
    
    # 자기자신의 체육복을 도난당했을시,
    lost, reserve = list(set(lost)-set(reserve)),list(set(reserve)-set(lost))
    
    for l in lost[:] :
        for r in reserve[:] :
            if l-r==-1 or l-r==1 :
                lost.remove(l)
                reserve.remove(r)
                break
    
    return n-len(lost)




