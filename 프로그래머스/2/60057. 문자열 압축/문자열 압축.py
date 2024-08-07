def solution(s):
    import sys
    answer = sys.maxsize
    for l in range(1, len(s)+1):
        result = ''
        s_dict = {}
        for i in range(0, len(s), l):
            if len(s_dict) == 0:
                s_dict[s[i:i+l]] = 1
            elif s[i:i+l] in s_dict:
                s_dict[s[i:i+l]] += 1
            else:
                s_1 = list(s_dict.keys())[0]
                s_2 = list(s_dict.values())[0]
                if s_2 == 1:
                    result += s_1
                else:
                    ss = str(s_2)+s_1
                    result += ss
                s_dict = {}
                s_dict[s[i:i+l]] = 1
        if len(s_dict) == 0:
            print(result, len(result))
        else:
            s_1 = list(s_dict.keys())[0]
            s_2 = list(s_dict.values())[0]
            if s_2 == 1:
                result += s_1
            else:
                ss = str(s_2)+s_1
                result += ss
        
        answer = min(answer, len(result))
    return answer