# 블랙잭
N, M = map(int, input().split())
card = list(map(int, input().split()))
num_max = 0
for i in range(N) : 
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            if card[i]+card[j]+card[k] <= M :
                if num_max < card[i]+card[j]+card[k] : 
                    num_max = card[i]+card[j]+card[k]
                
num_max

# 영화감독 숌
n = int(input())
t = 0
t_666 = 666
while True :
    if '666' in str(t_666) :
        t += 1
    if t == n :
        print(t_666)
        break
    t_666 += 1
    
    