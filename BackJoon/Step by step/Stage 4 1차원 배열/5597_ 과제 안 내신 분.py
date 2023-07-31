# 과제 제출 기한이 지났습니다.
id = [i for i in range (1, 31)]
for i in range(28) :
    N = int(input())
    id.remove(N)
    
    
print(min(id))        
print(max(id))   
