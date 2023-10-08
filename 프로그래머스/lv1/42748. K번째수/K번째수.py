def solution(array, commands):
    answer = []
    for c in commands :
        # i = 2, j = 5, k = 3
        i = c[0] - 1
        j = c[1]
        k = c[2] - 1
        arr = array[i : j]
        arr.sort()
        answer.append(arr[k])
    return answer