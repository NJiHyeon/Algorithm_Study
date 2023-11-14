def solution(arr1, arr2):
    answer = []
    import numpy as np
    arr2 = np.array(arr2).transpose().tolist()
    
    for i in range(len(arr1)) :
        li = []
        for j in range(len(arr2)) :
            ma = 0
            for k in range(len(arr1[0])) :
                ma += (arr1[i][k]*arr2[j][k])
            li.append(ma)    
        answer.append(li)       
    return answer