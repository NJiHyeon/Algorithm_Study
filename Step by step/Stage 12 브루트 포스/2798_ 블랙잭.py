# 세 장의 카드를 고르는 모든 경우를 고려하는 문제 ⭕
# 차이점 : 나는 세 숫자의 합과, M과 합의 차이를 모두 리스트에 넣어서 비교했는데, 그렇게 하지 않고 변수를 하나 만들어서 합이 더 큰 숫자로 갱신하는 방법을 생각하도록 고치자 !
# (즉, append -> a = max(a, sum))
#----------------------------------------------------------------------
from itertools import combinations
import sys
N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
combi_card = list(combinations(card, 3))

sum_list = []
minus_list = []

for i in range(len(combi_card)) :
    card_sum = combi_card[i][0]+combi_card[i][1]+combi_card[i][2]
    if card_sum <= M :
        sum_list.append(card_sum)


if M in sum_list : 
    print(M)
else :
    for i in range(len(sum_list)) : 
        minus = M - sum_list[i]
        minus_list.append(minus)
            
    min_index = minus_list.index(min(minus_list))
    print(sum_list[min_index])

#----------------------------------------------------------------------
# 다른 사람 풀이 1 
# for문을 이용해서 숫자 3개의 조합을 받고, 만약 숫자의 합이 M보다 크면 다시, 그렇지 않으면 그 전에 저장된 result(최댓값)과 합을 비교해 최댓값 갱신
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(N) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            if arr[i]+arr[j]+arr[k] > M :
                continue
            else :
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)
                
#----------------------------------------------------------------------
# 다른 사람 풀이 2
# 파이썬 제공 라이브러리를 이용해 숫자 3개의 조합을 받고, for문을 이용해 각각의 조합의 합을 구한 다음, 그 합이 그 전 결과보다 크고 K보다 작거나 같으면 최댓값 갱신
from itertools import combinations
N, K = map(int, input().split())
arr = list(map(int, input().split()))
sum_combination = list(combinations(card, 3))
result = 0

for cards in sum_combination :
    cards_sum = sum(cards)
    if result < cards_sum <= K :
        result = cards_sum

print(result)