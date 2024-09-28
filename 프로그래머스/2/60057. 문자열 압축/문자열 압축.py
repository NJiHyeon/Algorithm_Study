def solution(s):
    min_s = 1001
    for l in range(1, len(s)+1):
        stack = []
        l_s = ''
        for i in range(0, len(s), l):
            cur_s = s[i : i+l]
            if (stack and stack[-1] != cur_s):
                past_n = 0
                while stack:
                    past_s = stack.pop()
                    past_n += 1
                if past_n == 1:
                    l_s += past_s 
                else:
                    l_s += (str(past_n)+past_s)
            stack.append(cur_s)
        if len(stack) == 1:
            l_s += stack[-1]
        elif len(stack) >= 2:
            l_s += (str(len(stack))+stack[-1])
        min_s = min(min_s, len(l_s))
    return min_s