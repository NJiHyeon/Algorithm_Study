# OX 퀴즈의 결과를 일차원 배열로 입력받아 점수를 계산하는 문제
N = int(input())
score = 0
plus = 0
for i in range(N) :
    ox = list(input())
    for i in range(len(ox)) :
        if ox[i] == 'O' :
            plus = plus + 1
            score = score + plus
        else : 
            plus = 0
            score = score + plus
    print(score)
    score = 0
    plus = 0