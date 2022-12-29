# 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? (틀림)
# 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
sen = input()

cnt = 1
fcnt = 0
ecnt = 0
if sen[0] == ' ' :
    for i in sen :
        if i == ' ' :
            fcnt += 1

    print(fcnt)
    
elif sen[-1] == ' ' :
    for i in sen : 
        if i == ' ' :
            ecnt += 1
    print(ecnt)
    
else : 
    for i in sen :
        if i == ' ' :
            cnt += 1

    print(cnt)     


# 정답
# 1) 
word = input().split()
print(len(word))

# 2)
print(len(input().split()))