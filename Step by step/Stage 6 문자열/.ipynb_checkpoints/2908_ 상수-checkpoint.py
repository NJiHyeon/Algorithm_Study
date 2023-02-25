# 숫자를 뒤집어서 비교하는 문제 (맞음)
    # 숫자 인덱스 역수 취하는 코드는 외워두면 좋을 듯 !
    
a, b  = input().split()
a = int(a[::-1])
b = int(b[::-1])
if a > b :
    print(a)
    
else : 
    print(b)
    