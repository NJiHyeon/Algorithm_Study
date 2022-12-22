# 최솟값과 최댓값을 찾는 문제
    # Input 
        # 5
        # 20 10 35 30 7
    # Output : 7 35
    

N = int(input())
n = list(map(int, input().split()))
print(min(n), max(n))