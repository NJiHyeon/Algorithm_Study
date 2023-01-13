"""
층별로 누적합 구하기
"""

# 층과 거주자 수의 규칙을 찾는 문제
t = int(input())

for i in range(t) :
    k = int(input())
    n = int(input())
    
    # 새로운 리스트에 for문을 통해서 1~n까지 넣을 수 있다.
    people = [i for i in range(1, n+1)]
    
    for x in range(k) :
        new = []
        for y in range(n) :
            ii = sum(people[:y+1])
            new.append(ii)
        people = new.copy()
        
    print(people[-1])