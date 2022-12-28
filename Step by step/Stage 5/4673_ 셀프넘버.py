# 함수 d를 정의하여 문제를 해결해 봅시다.
# 틀림
origin_num = set(range(1, 10001))
make_num = set()

for i in range(1, 10001) :
    for j in str(i) :
        i += int(j)
    make_num.add(i)
    
self_num = sorted(origin_num - make_num)
for i in self_num :
    print(i)
    
self_num