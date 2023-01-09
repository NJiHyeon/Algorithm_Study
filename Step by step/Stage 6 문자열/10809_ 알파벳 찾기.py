# 알파벳 소문자로만 이루어진 단어 S가 주어진다. (틀림) 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 1) for
S = list(input())
C = 'abcdefghijklmnopqrstuvwxyz'
for i in C :
    if i in S :
        print(S.index(i), end='')
    else :
        print(-1, end='')
        
        
        
#2) find()
S = input()
for x in 'abcdefghijklmnopqrstuvwxyz' :
    print(S.find(x), end='')
    
    
    
#3) 아스키코드(이 방법은 헷갈리니까 pass)
S = input()
num = list(range(97, 123))
for i in num :
    print(S.find(chr(i)))