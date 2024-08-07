def solution(prices):
    # 스택 사용 (가격이 떨어지지 않으면 계속 쌓이므로, 떨어지는 것이 중점이므로 뒤에서부터 확인)
    answer = [len(prices)-k for k in range(1, len(prices)+1)] # 가격이 떨어지지 않았을 때 기간을 초기 설정
    stack = []
    for i in range(len(prices)) :
        while stack and prices[stack[-1]] > prices[i] :
            j = stack[-1] 
            stack.pop()
            answer[j] = i-j  #가격이 떨어지면 바꿔주기
        stack.append(i)

    return answer
