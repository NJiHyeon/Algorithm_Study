'''My code'''
n = int(input())
# 00시 00분 00초 ~ 5시 59분 59초까지 중 3 포함 개수
out = 0
for i in range(0, n+1) :
    for j in range(0, 60) :
        for k in range(0, 60) :
            if ('3' in str(i)) or ('3' in str(j)) or ('3' in str(k)) :
                out += 1
                
print(out)


'''Lecture code'''
# H 입력 받기
h = int(input())

count = 0
for i in range(h+1) :
    for j in range(60) :
        for k in range(60) :
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i)+str(j)+str(k) :
                count += 1
                
print(count)