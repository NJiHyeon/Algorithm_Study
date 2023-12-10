def solution(prices):
    # 스택 사용
    answer = [len(prices)-k for k in range(1, len(prices)+1)] 

    stack = []
    for i in range(len(prices)) :
        while stack and prices[stack[-1]] > prices[i] :
            j = stack[-1] 
            stack.pop()
            answer[j] = i-j 
        stack.append(i)

    return answer
