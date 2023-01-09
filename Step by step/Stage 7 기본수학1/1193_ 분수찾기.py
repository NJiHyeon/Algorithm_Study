# 분수의 순서에서 규칙을 찾는 문제
X = int(input())
layer = 1

while X > layer :
    X -= layer
    layer += 1
    
if layer % 2 == 0 :
    a = X
    b = layer - X + 1
else :
    a = layer - X + 1
    b = X
print(a,'/',b, sep='')