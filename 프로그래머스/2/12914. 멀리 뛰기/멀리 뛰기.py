def solution(n):
    ini = [0, 1, 2]
    if n==1 or n==2 :
        return ini[n]
    else :
        for i in range(n-2) :
            ini.append(ini[-1]+ini[-2])
    return ini[-1]%1234567