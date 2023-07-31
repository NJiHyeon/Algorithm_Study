### My code
N = int(input())
dong = [500, 100, 50, 10]

final = 0
for d in dong :
    if N//d >= 1 :
        n = N//d
        final += n
        N -= d*n
    else :
        pass
print(final)


---
### Lecture code
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array :
    # 혜당 화폐로 거술러 줄 수 있는 동전의 개수 세기
    count += n // coin
    n %= coin

print(count)


---
### 보완할 점
'''
- 변수의 이름을 헷갈리지 않게 하도록 잘 만들기 (몇 개 정해서 돌리는 것도 좋을듯)
- 나는 거슬러 주고 남은 돈을 (현재 남은 돈 = 이전 남은 돈 - 동전의 단위*개수)로 구했는데, 쉽게 %을 이용해서 현재 남은 돈을 몫을 나누고 나머지 값으로 설정하기 !
'''
