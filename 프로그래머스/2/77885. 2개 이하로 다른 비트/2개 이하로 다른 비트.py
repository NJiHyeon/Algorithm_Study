# 10진수를 하나씩 더하면서 2진수로 바꾸고 비교하는 완전탐색 방법으로 하면 무조건 시간초과 발생
# 짝수냐 홀수냐에 따라 2진수에서 그 다음 큰 수를 만들도록 바꾼 후 10진수로 변환해서 append 해주기
def solution(numbers) :
    answer = []
    for n in numbers :
        n_list = list('0' + format(n, 'b')) #리스트로 바꾸는 이유는 숫자를 바꿔야 하므로,
        idx = ''.join(n_list).rfind('0')
        n_list[idx] = '1'
        
        if n%2==1 :
            n_list[idx+1] = '0'
        answer.append(int(''.join(n_list), 2))
    return answer


# 이렇게 하면 시간초과,,, 그래도 잘 생각해 낸 방법 같아서 남겨둔다!
'''
def solution(numbers):
    answer = []
    for n in numbers :
        n_bit = format(n, 'b')
        new = n+1

        while True :
            new_bit = format(new, 'b')
            sum_bit = int(n_bit) + int(new_bit)
            c = str(sum_bit).count('1')
            if c == 1 or c == 2 :
                answer.append(new)
                break
            new += 1
    return answer
'''