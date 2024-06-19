def solution(str1, str2):
    import math
    answer = 0
    s1 = []
    s2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1)-1) :
        if str1[i:i+2].isalpha() :
            s1.append(str1[i:i+2])
    for j in range(len(str2)-1) :
        if str2[j:j+2].isalpha() :
            s2.append(str2[j:j+2])
        
    # 교집합 
    result1 = []
    s22 = s2.copy()
    for s in s1 :
        if s in s22 :
            s22.remove(s)
            result1.append(s)
    
    # 합집합
    # 일반적인 합집합
    result2 = []
    entire = list(set(s1)|set(s2))
    for e in entire :
        if s1.count(e) >= s2.count(e) :
            for l in range(s1.count(e)) :
                result2.append(e)
        else :
            for l in range(s2.count(e)) :
                result2.append(e)
            
    
    
    # 출력
    if len(result1)==len(result2)==0 :
        return 65536
    else :
        return math.floor((len(result1)/len(result2))*65536)
