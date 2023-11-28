def solution(numbers):
    result = [-1] * len(numbers)
    stack = [] #아직까지 큰 수를 찾지 못한 인덱스 저장소
    for i in range(len(numbers)) :
        while stack and numbers[i] > numbers[stack[-1]]: #stack이 비어 있지 않고 큰 수가 나타나면
            result[stack.pop()] = numbers[i]
        stack.append(i)
    return result