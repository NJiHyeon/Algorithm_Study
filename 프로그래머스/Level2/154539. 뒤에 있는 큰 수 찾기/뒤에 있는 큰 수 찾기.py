def solution(numbers):
    # 초기 리스트 설정
    result = [-1]*len(numbers)
    q = []
    for i in range(len(numbers)) :
        while q and numbers[q[-1]] < numbers[i] :
            result[q[-1]] = numbers[i]
            q.pop()
        q.append(i) #숫자를 넣으면 겹치므로 인덱스로 구분
    
    
    return result