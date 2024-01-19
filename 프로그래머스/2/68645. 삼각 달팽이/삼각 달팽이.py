def solution(n) :
    # num은 1씩 더하되, t의 위치를 찾아가면서 해당 num을 넣는다.
    t = [[0]*n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    
    for i in range(n) :
        for j in range(i, n) : #첫번째 for문을 돌 때마다, j의 개수는 (n, n-1, ...)
            # (1, 2, 3, 4, 5)
            # (6, 7, 8, 9)
            # (10, 11, 12)
            # (13, 14)
            # (15)
            if i%3 == 0 :
                #i는 0부터 시작되므로 x가 1씩 더해지니까 (0,0) 부터 시작되기 위해서는 x의 초기값이 -1이 되어야 함
                x += 1 
            elif i%3 == 1 :
                y += 1
            elif i%3 == 2 :
                x -= 1
                y -= 1
            t[x][y] = num
            num += 1
    
    for i in range(n) :
        for j in range(i+1) :
            answer.append(t[i][j])
    return answer