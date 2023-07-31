# 조건에 맞는 문자열을 찾는 문제
# 방법1) 
n = int(input())
group_number = n

for i in range(n) :
    sen = input()
    for j in range(0, len(sen)-1) :
        if sen[j] == sen[j+1] :
            pass
        elif sen[j] in sen[j+1:] :
            group_number -= 1
            break
        
print(group_number)
            
    
# 방법2) 우수코드
n = int(input())
group_number = 0

for i in range(n) :
    word = input()
    if list(word) == sorted(word, key=word.find) :
        group_number += 1
        
print(group_number)
