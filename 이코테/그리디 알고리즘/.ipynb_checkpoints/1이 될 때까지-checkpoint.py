### My code
n, k = map(int, input().split())

count = 0
while True :
    if n%k == 0 :
        n //= k
        count += 1 
        if n == 1 :
            break
            
    else :
        n -= 1
        count += 1
        if n == 1 :
            break
        
print("n :", n)
print("count :", count)


### Lecture code
# N, K를 공백을 기준으로 구분하여 입력받기
n, k = map(int, input().split())

result = 0

while True :
    '''
    N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    '''
    # target은 k로 나누어 떨어지는 수
    target = (n//k) * k
    # 1을 빼는 연산을 몇 번 수행할지 ?
    result += (n-target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k :
        break
    # K로 나누기
    result += 1
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)