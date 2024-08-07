def solution(n, arr1, arr2):
    new_arr1 = []
    new_arr2 = []
    for a in arr1 :
        na = n - len(bin(a)[2:])
        new_arr1.append('0'*na + bin(a)[2:])
    for b in arr2 :
        nb = n - len(bin(b)[2:])
        new_arr2.append('0'*nb + bin(b)[2:])
    
    mix = [''] * n
    
    for i in range(n) :
        for j in range(n) :
            if int(new_arr1[i][j]) + int(new_arr2[i][j]) == 0 :
                mix[i] += ' '
            else :
                mix[i] += '#'
                
    return mix
        