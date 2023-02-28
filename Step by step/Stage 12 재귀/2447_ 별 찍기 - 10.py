# 재귀적인 패턴을 재귀함수로 찍는 문제
# ---------------------------------------------------------------------------------------
import sys
sys.setrecursionlimit(10 ** 6)
# ---------------------------------------------------------------------------------------
# 1) 별을 9개의 공간으로 나눈뒤 1번 공간의 별이 5번 공간을 제외한 나머지 공간의 별에 똑같이 복사
n = int(sys.stdin.readline().strip())
g = [[' ' for _ in range(n)] for _ in range(n) ]

def paint_star(LEN) :
    DIV3 = LEN//3
    if LEN == 3 :
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*']*3
        return
    
    paint_star(DIV3)
    
    for i in range(0, LEN, DIV3) :
        for j in range(0, LEN, DIV3) :
            if i != DIV3 or j != DIV3 :
                for k in range(DIV3) :
                    g[i+k][j:j+DIV3] = g[k][:DIV3]
                    
paint_star(n)

for i in range(n) :
    for j in range(n) :
        print(g[i][j], end='')
    print()                   
    

# ---------------------------------------------------------------------------------------
# 2) 공간을 1, 2, 3으로 나눈 후 재귀함수를 통해 구해진 별을 붙인다(append)
"""
1. 제일 먼저 재귀적인 방법으로 n을 1까지 도달하게 한다음 ['*']을 리턴
2. 그러면 n=3일 때의 append_star(1)이 되므로 Stars는 ['*']이 되고 그 밑의 for문을 실행하게 된다.
"""
import sys
sys.setrecursionlimit(10**6)

def cycle_star(s) :
    if s == 1 :
        return ['*']
    
    star = cycle_star(s//3)
    L = []
    
    for i in star :
        L.append(i*3)
    for i in star :
        L.append(i + ' '* (s//3) + i)
    for i in star :
        L.append(i*3)
    
    return L

s = int(sys.stdin.readline().strip())
print('\n'.join(cycle_star(s)))

