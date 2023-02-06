# 재귀를 활용하여 정렬하는 방법을 배우는 문제 - 이해하는데 이틀이나 걸림....꼭 복습하기기!!!
# -----------------------------------------------------------------------------------------
# Googling Code
import sys
input = sys.stdin.readline
"""
merge_sort([4, 5])가 return L2 이므로 merge_sort([4, 5]) = [4, 5] 
merge_sort([1]) -> return L 이므로 merge_sort([1]) = [1] 
이런식으로 다시 돌아가면서(재귀) merge_sort[4, 5, 1, 3, 2]를 구할 수 있다. 
"""
def merge_sort(L) :
    if len(L) == 1 :
        return L
    
    mid = (len(L)+1)//2
    
    """
    계속 merge_sort를 호출하면서 반으로 나누기
    아래와 같이 호출하면 처음에 left로 나눠진 리스트 먼저 정렬되고, 
    right로 나눠진 리스트 정렬되고, left/right가 섞이면서 정렬된다.
    """
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    # print("len", len(L))
    # print("left", left)
    # print("right", right)
    """
    L2는 최종결과이므로 함수가 호출될때마다 리셋되야하므로 다시 []
    ans는 뭐가 차례대로 담기는지 순서대로 확인하기 위한 리스트
    """
    i, j = 0, 0
    L2 = []
    
    # left, right 리스트를 섞어서 비교
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            L2.append(left[i])
            ans.append(left[i])
            i += 1
        else : 
            L2.append(right[j])
            ans.append(right[j])
            j += 1

    """
    한쪽 방향의 리스트에만 작은 숫자들이 들어있었다면, 다른쪽은 리스트에 담기지 못했으므로
    다른쪽 방향도 남은 숫자들을 차례대로 정렬해주기 !
    """
    while i < len(left) :
        L2.append(left[i])
        ans.append(left[i])
        i += 1
    while j < len(right) :
        L2.append(right[j])
        ans.append(right[j])
        j += 1
        
    return L2
    
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = []
merge_sort(a)
if len(ans) >= k :
    print(ans[k-1])
else :
    print(-1)