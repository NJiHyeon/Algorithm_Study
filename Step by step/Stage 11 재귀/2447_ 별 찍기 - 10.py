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
import sys
sys.setrecursionlimit(10**6)

def append_star(LEN) :
    if LEN == 1 :
        return ['*']
    
    Stars = append_star(LEN//3)
    L = []
    
    for S in Stars :
        L.append(S*3)
        
    for S in Stars :
        L.append(S + ' ' * (LEN//3) + S)
    
    for S in Stars :
        L.append(S*3)
    
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))