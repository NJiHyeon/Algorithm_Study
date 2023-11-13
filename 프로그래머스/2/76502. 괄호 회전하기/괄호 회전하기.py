def solution(s):
    answer = 0
    if len(s)%2==1 :
        return 0
    else :
        for i in range(len(s)) :
            t = s[i:] + s[:i]
            for j in range(len(s)//2) :
                t=t.replace('()','')
                t=t.replace('{}','')
                t=t.replace('[]','')
            if len(t)==0 :
                answer += 1
        return answer