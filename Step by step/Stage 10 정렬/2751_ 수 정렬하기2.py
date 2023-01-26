# 시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있다.
# 예를 들면 병합정렬, 힙 정렬 등이 있지만, 지금은 언어에 내장된 정렬 함수를 쓰는 것을 추천 !
import sys
N = int(input())
num = []
for _ in range(N) :
    num.append(int(sys.stdin.readline()))
    
num.sort()

for i in range(N) :
    print(num[i])