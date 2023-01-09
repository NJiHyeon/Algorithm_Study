# 벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제

# 개수 받기
n = int(input())
# 한바퀴 돌때마다 더할 변수
number = 1
# print할(몇번 거치는지)
cnt = 1

# n이 number보다 크면 계속 반복
while n > number :
    # 6의 배수 개수만큼 도니까, number = number + 6*cnt
    number += 6*cnt
    # 한바퀴 돌면 거쳐가는 개수 1씩 더해주기
    cnt += 1
    
print(cnt)