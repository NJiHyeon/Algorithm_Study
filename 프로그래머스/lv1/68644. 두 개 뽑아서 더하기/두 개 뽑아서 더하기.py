def solution(numbers):
    answer = []
    for i in range(len(numbers)) :
        for j in numbers[i+1:] :
            if numbers[i]+j not in answer :
                answer.append(numbers[i]+j)
    answer.sort()
    return answer