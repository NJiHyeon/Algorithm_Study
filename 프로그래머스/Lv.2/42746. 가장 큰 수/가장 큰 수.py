def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse=True) #1000이하의 수이므로, 최소1/최대3의 자리수니까
    answer = ''.join(numbers)
    return str(int(answer))