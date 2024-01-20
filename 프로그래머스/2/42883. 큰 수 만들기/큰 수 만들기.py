def solution(number, k):
    stack = []
    l = len(number)
    for i in range(len(number)) :
        while k>0 and stack and stack[-1]<number[i] :
            k -= 1
            stack.pop()
        stack.append(number[i])
    return ''.join(stack[:l-k])