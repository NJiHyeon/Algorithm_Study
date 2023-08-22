'''
- dfs 함수는 지정된 위치에서 (초기값) 반복적으로 재귀하면서 확인
- for문은 전체 데이터에 대해 확인
=> 두 과정을 수행하면 겹칠 수 있는 값이 존재하는데 이것을 return True/False로 처리 ! (한번 다 수행하면 return True)
'''
# 음료수칸 만들기
n, m = map(int, input().split())
drink = []
for i in range(n) :
    drink.append(list(map(int, input())))
    
# 모든 경우의 수를 탐색해야 하므로 DFS 사용
def dfs(x, y) :
    # 만약 i,j의 위치가 얼음틀의 범위를 벗어나지 않으면 계속 수행
    # 재귀함수 : 상하좌우 (방문처리는 필수!)
    if x<=-1 or x>=n or y<=-1 or y>=m :
        return False
    if drink[x][y] == 0 :
        drink[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# drink 리스트에 있는 값을 한번씩 돌면서 함수 처리 => 끝나면 아이스크림 1개 생성 (return)
ice = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            ice += 1  
print(ice)