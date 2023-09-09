arr = [1,1,3,3,0,1,1]
def solution(arr):
    for i in range(len(arr)-1) :
        if arr[i] == arr[i+1] :
            arr[i] = 11
        else :
            pass
    rm_set = {11}
    arr_new = [i for i in arr if i not in rm_set]
    return arr_new

# 새로운 리스트를 만들어서 추가하는 방식으로 만들어보기!