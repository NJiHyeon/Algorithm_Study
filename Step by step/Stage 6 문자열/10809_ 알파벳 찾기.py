# 알파벳 소문자로만 이루어진 단어 S가 주어진다. (틀림) 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 1) 리스트로 인덱스 찾기
S1 = list(input())
C = 'abcdefghijklmnopqrstuvwxyz'
for i in C :
    if i in S1 :
        print(S1.index(i), end='')
    else :
        print(-1, end='')

# 2) find 함수 사용
S2 = input()  
C = 'abcdefghijklmnopqrstuvwxyz'      
for i in C :
    print(S2.find(i), end='')
    
'n' in S1   
'n' in S2        

    
