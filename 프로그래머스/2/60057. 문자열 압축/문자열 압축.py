def solution(s):
    min_l = 1001
    for unit in range(1, len(s)+1): #단위
        cur_s = ''
        cur_n = 0
        unit_s = ''
        for index in range(0, len(s), unit): #앞에서부터
            if cur_s == '':
                cur_s = s[index : index+unit]
                cur_n = 1
            elif cur_s == s[index : index+unit]:
                cur_n += 1
            else:
                if cur_n == 1:
                    unit_s += cur_s
                else:
                    unit_s += (str(cur_n)+cur_s)
                cur_n = 1
                cur_s = s[index : index+unit]
        
        if cur_n == 1:
            unit_s += cur_s
        else:
            unit_s += (str(cur_n)+cur_s)
                
        min_l = min(min_l, len(unit_s))
    return min_l
            