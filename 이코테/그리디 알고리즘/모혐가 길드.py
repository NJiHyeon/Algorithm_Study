n = int(input())
gong = list(map(int, input().split()))
gong.sort()

group_n = 0 # 총 그룹의 수
people_n = 0 # 현재 그룹에 포함된 모험가의 수

for i in gong : # 공포도를 낮은 것부터 하나씩 확인
    people_n += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if i <= people_n : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        group_n += 1 # 총 그룹의 수 증가
        people_n = 0 # 현재 그룹에 포함된 모험가의 수 초기화
        
# 총 그룹의 수 출력
print(group_n)