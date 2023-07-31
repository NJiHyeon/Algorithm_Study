# 각 문자를 반복하여 출력하는 문제 (틀림)
"""
방법1
: 문자열의 길이만큼 반복
  -> 문자열의 인덱스 * 개수
  
방법2
: 직접 문자열을 하나씩 받아서 반복
  -> 하나씩 받아서 * 개수

"""
T = int(input())
for i in range(T) :
        N, C = input().split()
        for i in range(0, len(C)) :
            print(C[i]*int(N), end='')
        print() ## 중요중요


        
T = int(input())
for i in range(T) :
        N, C = input().split()
        for j in C :
            print(j*int(N), end='')
        print() ## 중요중요